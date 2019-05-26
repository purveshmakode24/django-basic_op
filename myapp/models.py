from django.db import models

# Create your models here.
class Employee(models.Model):
	ename = models.CharField(max_length=20, primary_key=True)
	esalary = models.CharField(max_length=10)