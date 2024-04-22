from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "home.html")
print(home)

def about(request):
    return render(request, "about.html")
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
