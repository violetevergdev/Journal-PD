import sqlite3


def run_query(query, parameters=()):
    # with sqlite3.connect('pfr.db') as conn:
    with sqlite3.connect('W:\\!VIOLETTA!\\!fw!\\journal\\journal.db') as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)
        conn.commit()
    return result
