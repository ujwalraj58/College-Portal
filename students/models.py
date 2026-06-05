from django.db import models

class Student(models.Model):
    roll_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='students/', blank=True, null=True)
    password = models.CharField(max_length=100, default='password')

    def __str__(self):
        return self.roll_no