from django.db import models

# Create your models here.
# anytime you modify the models you MUST make and run migrations
#you need to register your newly created models in the admin file

class Product(models.Model):
    product_name = models.CharField(max_length=50, null=False, blank=False)
    product_price = models.DecimalField(max_digits=100, decimal_places=4)
    product_description = models.TextField(null=False, blank=False)
    product_image = models.ImageField(upload_to='product_images', default='product_images/back2.JPG')
    
    def __str__(self):
        return self.product_name
    
    
    
class Teacher(models.Model):
    name =models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    age = models.DecimalField(max_digits=20, blank=False, decimal_places=1)
        
    def __str__(self):
        return self.name