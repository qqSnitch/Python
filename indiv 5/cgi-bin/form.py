import cgi
form =cgi.FieldStorage()
text1 = form.getfirst("Name", "Empty")
text2 = form.getfirst("Title", "Empty")
text3 = form.getfirst("Salary", "Empty")
print("Content-type: text/html")
print("""<!DOCTYPE HTML>
<html>
<head>
<meta charset="cp1251">
<title>Agency </title>
</head>
<body>""")
print("<h1>Agency data</h1>")
print("<p>Name: %s</p>"%text1)
print("<p>Title: %s</p>"%text2)
print("<p>Salary: %s</p>"%text3)
print("""</body> </html>""")