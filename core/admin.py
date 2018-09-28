from django.contrib import admin
from .models import Watches, Order, OrderPosition, NameBrand, Cart, CartItem

# Register your models here.
class NameBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Watches)
admin.site.register(NameBrand)
admin.site.register(Order)
admin.site.register(OrderPosition)
admin.site.register(Cart)
admin.site.register(CartItem)
