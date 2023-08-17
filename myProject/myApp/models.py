from django.db import models

# Create your models here.
class myData(models.Model):
    Name=models.CharField(max_length=30,null=False,blank=False);
    Age=models.IntegerField(null=False,blank=False);
    Email=models.EmailField(null=False,blank=False);
    Phone=models.IntegerField(null=False,blank=False);
    
