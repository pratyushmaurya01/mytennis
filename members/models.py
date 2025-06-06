from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.IntegerField()
    joined_date = models.DateField()
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
