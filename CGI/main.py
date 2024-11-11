import sqlite3
con = sqlite3.connect('db01.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS books') #удаление в случае,
#если таблица существует
cur.execute('CREATE TABLE books(id INTEGER PRIMARY KEY,title VARCHAR(30),author VARCHAR(30), persTEXT)')
cur.execute('CREATE TABLE IF NOT EXISTS books(i INTEGER PRIMARY KEY,title VARCHAR(30), author VARCHAR(30),pers TEXT)')#создание таблицы,
#если она не была создана ранее
print (cur.lastrowid)
cur.execute('SELECT * FROM books')
print(cur.fetchall())