from django.contrib import admin
from .models import Watches, Orders, NameBrand

# Register your models here.
class NameBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Watches)
admin.site.register(NameBrand)
admin.site.register(Orders)