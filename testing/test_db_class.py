import os
import threading
from datetime import datetime

import pytest
from contextlib import nullcontext as does_not_raise
from modules.db.db_connection import Database
from modules.optionally.logging_db import logging_db


class TestDBClass:
    @pytest.fixture(scope="function")
    def setup_method(self):
        log = logging_db()
        db = Database(None)
        record_values = ['t10', 't1', 't2', 't1', 't2', 't3', 't4', 't5', 't6', '', '', '', '', 't15', 't71', 't22', 't35']
        yield log, db, record_values
        db.run_query('DELETE FROM pfr WHERE СНИЛС > 0', log, None)

    def test_multithreaded_connections(self, setup_method):
        log, db, record_values = setup_method
        threads = []
        for i in range(50):
            t = threading.Thread(target=db.add_new_record, args=(log, None, record_values))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        res = db.get_all_records(log, None)
        assert len(res[0]) == 50

    def test_edit_record(self, setup_method):
        log, db, record_values = setup_method
        edit_values = ['t001', 't1', 't2', 't91', 't2', 't3', 't4', 't500', 't6', '', '', '', '', 't31', 't15', 't21', 't53']

        res = db.add_new_record(log, None, record_values)
        assert res is True

        all_data = db.get_all_records(log, None)
        assert all_data[0][0][1] == record_values[0]

        update_res = db.update_record(log, None, edit_values, 1)
        assert update_res is True

        all_data = db.get_all_records(log, None)
        assert all_data[0][0][1] == edit_values[0] and all_data[0][0][8] == edit_values[7]

    def test_delete_record(self, setup_method):
        log, db, record_values = setup_method
        del_id = 3

        for i in range(5):
            db.add_new_record(log, None, record_values)

        res = db.get_all_records(log, None)
        assert len(res[0]) == 5

        db.delete_record(log, None, del_id)
        res = db.get_all_records(log, None)
        assert len(res[0]) == 4 and res[0][1][0] == 2 and res[0][2][0] == 4

    def test_find_record(self, setup_method):
        log, db, record_values = setup_method
        db.add_new_record(log, None, record_values)
        res = db.find_records(log, None, "СНИЛС", "2")
        assert len(res[0]) == 1 and res[0][0][5] == 't2'

        for _ in range(3):
            db.add_new_record(log, None, record_values)

        res = db.find_records(log, None, 'Район', '1')
        assert len(res[0]) == 4 and res[0][0][4] == 't1' and res[0][2][4] == 't1'

    @pytest.mark.parametrize(
        'bank, exp',
        [
            ('Новый Банк', does_not_raise()),
            ('АО "ГАЗПРОМБАНК"', pytest.raises(AssertionError)),
        ]
    )
    def test_add_bank(self, setup_method, bank, exp):
        log, db, _ = setup_method
        with exp:
            try:
                res = db.add_bank(log, None, bank)
                if not res:
                    raise AssertionError('Такой банк уже есть')
            finally:
                db.run_query('DELETE FROM banks WHERE Наименование == "Новый Банк"', log, None)
