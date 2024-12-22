from django.db import models


class Employer(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Agency(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    salary = models.IntegerField()

    def __str__(self):
        return self.name

class Contract(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)

    def __str__(self):
        return f"Contract between {self.employer} and {self.agency}"


    # cur.execute('''CREATE TABLE Employers(
    #             id INTEGER PRIMARY KEY AUTOINCREMENT,
    #             name VARCHAR(30),
    #             surname VARCHAR(30),
    #             email VARCHAR(30),
    #             phone VARCHAR(30))''')
    # cur.execute('''CREATE TABLE IF NOT EXISTS Agency(
    #             id INTEGER PRIMARY KEY AUTOINCREMENT,
    #             name VARCHAR(30),
    #             title VARCHAR(30),
    #             salary INTEGER)''')
    # cur.execute('''CREATE TABLE IF NOT EXISTS Contracts(
    #             id INTEGER PRIMARY KEY AUTOINCREMENT,
    #             employerId INTEGER,
    #             agencyId INTEGER)''')