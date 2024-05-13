from django.contrib import admin
from . models import Product
from . models import Teacher


# Register your models here.

admin.site.register(Product)
admin.site.register(Teacher)


#Create, read, update, delete