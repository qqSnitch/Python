import cgi
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

name = form.getfirst("Name", "Empty")
title = form.getfirst("Title", "Empty")
salary = form.getfirst("Salary", "Empty")

print("Content-type: text/html")
print("""
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Agency Data</title>
</head>
<body>
<h1>Agency Data</h1>
<p>Name: %s </p>"""%name)
print("<p>Title: %s</p>"%title)
print("<p>Salary: %s</p>"%salary)
print("""</body>
</html>
""")

