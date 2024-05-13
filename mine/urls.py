from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('project/', views.project, name='project'),
    path('services/', views.services, name='services'),
    path('insert_product/', views.insert_product, name='insert_product'),
    path('products/', views.products, name='products')    
]
