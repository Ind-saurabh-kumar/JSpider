from django.db import models

# Create your models here.



class EmployeeData(models.Model):
    
    empId=models.IntegerField(primary_key=True, max_length=10)
    empName=models.CharField(max_length=30)
    empSal=models.IntegerField(max_length=30)



