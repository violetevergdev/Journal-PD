
# Журнал

Программа для ведения журнала пенсионнных дел

<img src="https://img.shields.io/badge/Version-1.2.2-red" alt="Version">
<img src="https://img.shields.io/badge/License-MIT-brightgreen" alt="License">


## Содержание
- [Технологии](#технологии)
- [Использование](#использование)
    * [Настройка перед использованием](#настройка-перед-использованием)
    * [Использование](#использование)
- [Разработка](#разработка)
    * [Компиляция](#компиляция)
- [Содержание конфигурационных файлов](#содержание-конфигурационных-файлов)


## Технологии
- [Python 3.8.7](https://www.python.org/downloads/release/python-387/)
- [PyQt5](https://www.riverbankcomputing.com/software/pyqt/)
- [sqlite3](https://docs.python.org/3/library/sqlite3.html)
- [pandas](https://pandas.pydata.org/)

## Использование

#### Настройка перед использованием

Для работы необходимо разархивировать в удобное для вас место, архив ``Journal - v... (compiled)`` (находятся в Releases)

Также для запуска необходимо иметь на диске `W:\!VIOLETTA!\!fw!\journal` файл `settings.toml`, его вы можете взять в исходниках проекта. (Либо указать свое расположение в `configuration\config.py` и перекомпилировать)

### Использование

#### Основные функции:

Для управления данными используются три основные кнопки в самом низу окна. 

  * Добавление новой записи:
  
    Форма для добавления записи имеет ряд ограничений: 
    1.	Поля со * являются обязательными для заполнения; 
    2.	Поле Район ограничен по максимальной длине символов (до 3х);
    3.	Поле СНИЛС допускает ввод 14 символов с добавлением спец. знаков (123-123-123 12);
    4.	Поле ФИО Пенсионера допускает ввод в форматах: Фамилия И.О./ФАМИЛИЯ ИО и тп., ввод Фамилия Имя Отчество выдаст ошибку.

    > Для того чтобы выбрать Банк необходимо нажать на кнопку «+» рядом с полем Банк,  вам откроется список централизованных банков. С целью удобного пользования вверху окна имеется поле для поиска, достаточно написать в нем ВТБ, чтобы в списке отобразился Филиал № 7701 Банка ВТБ (ПАО). 
  
    > Если вы не нашли в списке необходимый вам банк,  вы можете добавить его самостоятельно посредством нажатия на кнопку «Новый Банк», после чего появится окно, в которое нужно внести наименование банка, после чего он отобразится в самом конце списка. 
  
    > Будьте очень внимательны при добавлении новых банков, чтобы исключить появления дублирующих значений в списке. 
  
    > Форма добавления новой записи допускает множественного использования, т.е. после добавления записи форма не закроется, а очиститься и предложит ввести новые значения с одним НО! Для удобства использования некоторые поля не подводятся под очищение, а именно: Очередность выплаты, Выплатной месяц, Специалист О.В., Дата отработки.

  * Изменение записи:
    > Для того чтобы изменить уже созданную запись, необходимо ЛКМ выбрать нужную запись в таблице и нажать «Изменить». Вам откроется привычная форма для добавления, но с уже заполненными полями. После успешного сохранения изменений появится информационное окно и изменения отобразятся в таблице.

  * Удаление записи:
    > Для удаления записи ее также необходимо выбрать и после нажать «Удалить», программа запросит ввод пароля, его уточняйте у системного администратора.

#### Дополнительная функциональность
* Выгрузка таблицы:
    > Для выгрузки таблицы в Excel в верхнем меню выберите «Выгрузить», программа запросит ввод пароля, после его ввода укажите путь для сохранения файла. Рекомендуется переименовывать выгруженный файл, т.к. если при повторной выгрузке вы укажете тот же путь, этот файл может перезаписаться.

* Отслеживание обновлений:
    > Кнопка «Обновить» необходима, если вам нужно посмотреть, были ли внесены новые записи другими пользователями или сбросить результаты поиска.

* Поиск:
    
Поиск осуществляется по следующим столбцам:
1.	СНИЛС; 
2.	ФИО Пенсионера; 
3.	Специалист О.В.
4.	Район;
5.	Очередность выплаты;
6.	Выплатной месяц.


## Разработка

### Компиляция:
```sh
pyinstaller --onefile --hidden-import "babel.numbers" --windowed --name Журнал main.py   
```

```sh
pyinstaller  Журнал.spec
```