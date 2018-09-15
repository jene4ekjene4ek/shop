from django.db import models




# Create your models here.



class Watches(models.Model):

    MEN = 0
    WOMEN = 1
    UNISEX = 2

    GENDER_CHOICES = (
        (MEN, 'Men'),
        (WOMEN, 'Women'),
        (UNISEX, 'Unisex')
    )

    SWISS = 0
    EUROPE = 1
    JAPAN = 2

    COUNTRY_CHOICES = (
        (SWISS, 'Swiss'),
        (EUROPE, 'Europe'),
        (JAPAN, 'Japan')
    )
    #brand_id = models.ForeignKey(Brands)
    title = models.CharField(max_length = 250)
    subtitle = models.CharField(max_length = 250)
    price = models.FloatField() 
    date_add = models.DateField(auto_now_add=False)
    fashion = models.BooleanField(default=False)
    #sex = models.CharField(default=True, max_length = 250)
    char = models.TextField(default=True)
    image = models.ImageField(default=True, upload_to="img")
    slug = models.SlugField(default=True)
    gender = models.IntegerField(null=True, choices=GENDER_CHOICES)
    made_by = models.IntegerField(null=True, choices=COUNTRY_CHOICES)


    def __str__(self):
        return self.title

class Orders(models.Model):
    #id_user
    #id_watch
    quantity = models.FloatField()
    summ = models.FloatField()
    date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length = 250)



# class NameBrand(models.Model):
#     name = models.CharField(max_length = 50)

    

