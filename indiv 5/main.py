import sqlite3
con = sqlite3.connect('HH.db')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS Employers')
cur.execute('DROP TABLE IF EXISTS Agency')
cur.execute('DROP TABLE IF EXISTS Contracts')
cur.fetchall()
cur.execute('''CREATE TABLE Employers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(30),
            surname VARCHAR(30),
            email VARCHAR(30),
            phone VARCHAR(30))''')
cur.execute('''CREATE TABLE IF NOT EXISTS Agency(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(30),
            title VARCHAR(30),
            salary INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Contracts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employerId INTEGER,
            agencyId INTEGER)''')

employers=[
    ("Bob","Bobov","BobBobov@gmail.com","+1234567890"),
    ("John","Johnson","JohnJohnson@gmail.com","+2345678901"),
    ("Ivan","Ivanov","IvanIvanov@gmail.com","+3456789012")
]
agency=[
    ("T-bank","Developer","80000"),
    ("CarX","Game Designer","60000"),
    ("MedRocket","QA Engineer","90000")
]
contracts=[
    (1,2),
    (3,3),
    (2,1)
]

sqlE='''INSERT INTO Employers(name,surname,email,phone) VALUES (?,?,?,?)'''
sqlA='''INSERT INTO Agency(name,title,salary) VALUES (?,?,?)'''
sqlC='''INSERT INTO Contracts(employerId,agencyId) VALUES (?,?)'''

cur.executemany(sqlE,employers)
cur.executemany(sqlA,agency)
cur.executemany(sqlC,contracts)

con.commit()

cur.execute('SELECT * FROM employers ORDER BY name ASC')
print(cur.fetchall())
cur.execute('SELECT * FROM agency WHERE salary>70000')
print(cur.fetchall())
cur.execute('SELECT * FROM agency')
print(cur.fetchall())
