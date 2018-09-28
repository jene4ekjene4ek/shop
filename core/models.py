from django.db import models




# Create your models here.

class NameBrand(models.Model):
    name = models.CharField(max_length = 50, unique=True)
    slug = models.SlugField(default=True, unique=True)
    image = models.ImageField(default=False, upload_to="img")


    def __str__(self):
            return self.name

class Watches(models.Model):

    MEN = 'M'
    WOMEN = 'W'
    UNISEX = 'U'

    GENDER_CHOICES = (
        (MEN, 'Men'),
        (WOMEN, 'Women'),
        (UNISEX, 'Unisex')
    )

    SWISS = 0
    EUROPE = 1
    JAPAN = 2

    COUNTRY_CHOICES = (
        (SWISS, 'Швейцарские'),
        (EUROPE, 'Европейские'),
        (JAPAN, 'Японские')
    )

    KVARTZ = 0
    MECHAN = 1
    MECHAN_AVTO = 2
    AVTOKVARTZ = 3
    KVARTZ_MECHAN_AVTO = 4


    MECHANISM_CHOICES = (
        (KVARTZ, 'Кварцевый'),
        (MECHAN, 'Механический'),
        (MECHAN_AVTO, 'Механический с автоподзаводом'),
        (AVTOKVARTZ, 'Автокварцевый'),
        (KVARTZ_MECHAN_AVTO, 'Кварцевый + механический с автоподзаводом')
    )


    ALUM = 0
    GOLD = 1
    KERAM = 2
    KERAM_STEEL = 3
    METALL = 4
    METALL_GOLD = 5
    METALL_POLIMER = 6

    KORPUS_CHOICES = (
        (ALUM, 'Алюминий'),
        (GOLD, 'Золото'),
        (KERAM, 'Керамика'),
        (KERAM_STEEL, 'Керамика+сталь'),
        (METALL, 'Металл'),
        (METALL_GOLD, 'Металл+позолота'),
        (METALL_POLIMER, 'Металл-полимер')
    )


    namebrand = models.ForeignKey(NameBrand, default=True, on_delete=models.CASCADE)
    title = models.CharField(max_length = 250)
    subtitle = models.CharField(max_length = 250)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date_add = models.DateField(auto_now_add=False)
    fashion = models.BooleanField(default=False)
    
    char = models.TextField(default=True)
    image = models.ImageField(default=True, upload_to="img")
    slug = models.SlugField(default=True, unique=True)
    gender = models.CharField(null=True, choices=GENDER_CHOICES, max_length=1)
    made_by = models.IntegerField(null=True, choices=COUNTRY_CHOICES)
    mechanism = models.IntegerField(null=True, choices=MECHANISM_CHOICES)
    korpus = models.IntegerField(null=True, choices=KORPUS_CHOICES)
    discount = models.FloatField(default=False) 
    status = models.BooleanField(default=True)

    


    def __str__(self):
        return self.title

class CartItem(models.Model):
    watch = models.ForeignKey(Watches)
    quantity = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.watch.title

class Cart(models.Model):
    items = models.ManyToManyField(CartItem, blank=True)
    cart_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.id

    # def add_to_cart(self, watch_slug):
        

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Opened at")
    closed_at = models.DateTimeField(verbose_name="Closed at", blank=True, null=True)
    is_closed = models.BooleanField(default=False)
    


    def price(self):
        total_price = 0
        for p in self.positions.all():
            total_price += p.price()
        return total_price

class OrderPosition(models.Model):
    order = models.ForeignKey(Order, related_name="positions")
    watches = models.ForeignKey(Watches)
    quantity = models.PositiveIntegerField(default=1)

    def price(self):
        return self.watches.price * self.quantity