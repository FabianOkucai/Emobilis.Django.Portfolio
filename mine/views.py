from django.shortcuts import render
from django.http import HttpResponse
from . models import Product

# Create your views here.


def home(request):
    return render(request, "home.html")
print(home)


def about(request):    return render(request, "about.html")
print(about)


def contact(request):
    return render(request, "contact.html")
print(contact)


def services(request):
    return render(request, "services.html")
print(services)


def project(request):
    return render(request, "project.html")
print(project)

def insert_product(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        product_price = request.POST['product_price']
        product_description = request.POST.get('product_description', '')

        if 'product_image' in request.FILES:
            product_image = request.FILES['product_image']
            product = Product(product_name=product_name, 
                              product_price=product_price, 
                              product_description=product_description, 
                              product_image=product_image)
            product.save()
        else:

            pass
    
    return render(request, "insert_product.html")
print(insert_product)


def products(request):
    data = Product.objects.all()
    return render(request, "products.html", {'products': data})
print(products)







