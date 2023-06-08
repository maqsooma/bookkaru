from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import datetime

# Create your models here.


class Service(models.Model):
    
    start_from = models.CharField(max_length=200,null=True,blank=True)
    ends_at =  models.CharField(max_length=200,null=True,blank=True)
    date = models.DateField(editable=False,blank=True,null=True)
    operator = models.CharField(max_length=200,null=True,blank=True)
    
    srevicetype = ArrayField(models.CharField(max_length=100),blank = True, default = list)
    
    price = models.IntegerField(blank=True,default=None)
    
    amenities = models.IntegerField(blank=True,null=True)
    

    
    
    class Meta:
        ordering = ('operator',)
        
    def __str__(self):
        return self.operator