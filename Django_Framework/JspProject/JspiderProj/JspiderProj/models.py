

from django.db import models

class Product:
    pass



class Faculty(models.Model):
    fId=models.IntegerField()
    fName=models.CharField(max_length=20)
    fDept=models.CharField(max_length=20)
    
    
    
    
    
    
    
    

