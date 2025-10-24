from django.contrib.auth.models import AbstractUser
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Designation(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Users(AbstractUser):
    employee_id = models.CharField(max_length=50, unique=True, null=True, blank=True)
    
    # ForeignKey relationships
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True, blank=True)

    gender = models.CharField(max_length=10, choices=[("male", "Male"), ("female", "Female")], default="male")
    birthdate = models.DateField(null=True, blank=True)
    marital_status = models.CharField(max_length=20, choices=[("Married", "Married"), ("Un-Married", "Un-Married")], blank=True, null=True)
    blood_grp = models.CharField(max_length=50, null=True, blank=True)

    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
