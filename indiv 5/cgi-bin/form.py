# <Data></Data>

import cgi
import cgitb
cgitb.enable()
import sqlite3
import xml.etree.ElementTree as xml

con = sqlite3.connect('HH.db')
cur = con.cursor()
form = cgi.FieldStorage()
name = form.getfirst("Name", "Empty")
title = form.getfirst("Title", "Empty")
salary = form.getfirst("Salary", "Empty")

tree = xml.parse('table.xml')
root = tree.getroot()

agencyEl=xml.SubElement(root,"Agency")

nameEl = xml.SubElement(agencyEl,"Name")
nameEl.text=name

titleEl = xml.SubElement(agencyEl,"Title")
titleEl.text=title

salaryEl = xml.SubElement(agencyEl,"Salary")
salaryEl.text=str(salary)

tree.write('table.xml')

table=root.iter()
arg=[]
for child in root:
    print(child.tag)
    print("<br>")
    if child.tag == "Agency":
        for step_child in child:
            arg.append(step_child.text)
    sql1 = '''INSERT INTO agency (name,title,salary) VALUES(?,?,?)'''
    cur.execute(sql1, arg)
    arg=[]

    con.commit()


print("""
<!DOCTYPE HTML>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>Данные агентства</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; }
        h1 { color: #333; }
        table {
            border-collapse: collapse;
            width: 100%;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
            font-weight: bold;
        }
        .button {
            display: inline-block;
            border-radius: 4px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            padding: 10px 30px;
            margin: 10px 5px;
            transition: background-color 0.3s;
        }
        .button:hover {
            background-color: #45a049;
        }
    </style>
</head>""")

print("""
<body>
<table>
    <h>Таблица из БД</h>
    <tr>
        <th>ID</th>
        <th>Название</th>
        <th>Должность</th>
        <th>Зарплата</th>
    </tr>
""")
cur.execute('SELECT * FROM agency')
for row in cur.fetchall():
    print(f"""
    <tr> 
        <td>{row[0]}</td>
        <td>{row[1]}</td>
        <td>{row[2]}</td>
        <td>{row[3]}</td>
    </tr>""")
print("""</table>""")
print("""
</body>
</html>""")