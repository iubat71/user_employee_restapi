
from django.db import models

# Create your models here.

class Employees(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_mobile = models.TextField()
    emp_email = models.TextField(null = True)
    
