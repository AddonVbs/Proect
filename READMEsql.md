## ИСПОЛЬЗОВАНИЕ SQLite
1) скачеваем все нужное https://sqlite.org/download.html
    листаем в низ и находим 
    Precompiled Binaries for Windows
    далее скачиваем - sqlite-dll-win-x64-3490100.zip (1.28 MiB)
    создаем папку на рабочем столе и перетаскиываем туда все файла с  sqlite-dll-win-x64-3490100.zip (1.28 MiB)

2) скачиваем на этом же сайте - sqlite-tools-win-x64-3490100.zip(6.12 MiB)
    скачали открыли, и ТОЛЬКО перетаскиваем sqlite3.exe (вместо 3 может быть и 2 ) в нашу папку на рабочем столе

## КОМАНДЫ ДЛЯ sqlite3.exe
1) .open (и название таблици) = (создает таблицу или открывает таблицу)

2)  CREATE TABLE user (
        //id INTEGER PRIMARY KEY AUTOINCREMENT,
        //name VARCHAR(70),
        //password VARCHAR(80)); 

    =(создает таблицу и водить нужные данные)
    // = нужные данные 

3) .tables = (показывает скок таблиц существет)

4) .schema (название таблици) = (позволяет посмтреть что под капотом в твблице)

5) SELECT * FROM (ваша таблица) = (посмотреть всех пользователей,зареганых)





## РАНДОМ ЗАПИСИ ДЛЯ ТЕСТА

1)  INSERT INTO user (name,password)
    VALUES ('Kikit3245', '2311777');

2)  INSERT INTO user (name,password)
    VALUES ('lolipop3345', '1818187');
