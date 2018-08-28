from django.db import models


# Create your models here.

class Watches(models.Model):
    title = models.CharField(max_length = 250)
    subtitle = models.CharField(max_length = 250)
    price = models.FloatField()
    
   
    date_add = models.DateTimeField(blank=True, null=True)
    fashion = models.BooleanField(default=False)
   


    def __str__(self):
        return self.title

