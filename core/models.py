from django.db import models




# Create your models here.

class Watches(models.Model):

    MALE = 0
    FEMALE = 1
    UNISEX = 2

    SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (UNISEX, 'Unisex')
    )



    title = models.CharField(max_length = 250)
    subtitle = models.CharField(max_length = 250)
    price = models.FloatField() 
    date_add = models.DateField(auto_now_add=False)
    fashion = models.BooleanField(default=False)
    #sex = models.CharField(default=True, max_length = 250)
    char = models.TextField(default=True)
    image = models.ImageField(default=True, upload_to="img")
    slug = models.SlugField(default=True)

    sex = models.IntegerField(null=True, choices=SEX_CHOICES)
   
    def __str__(self):
        return self.title

class Orders(models.Model):
    #id_user
    #id_watch
    quantity = models.FloatField()
    summ = models.FloatField()
    date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length = 250)

    

