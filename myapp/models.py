from django.db import models

# Create your models here.
class Employee(models.Model):
	ename = models.CharField(max_length=20)
	esalary = models.CharField(max_length=10)