import os
import django
from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product
from math import ceil

# Allowing sync_to_asyn so as to retrieve the data from the database
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup() 

# function for the index.html file
def index(request):

# list of all the products      # cats: category list
    prod = Product.objects.all()                
    cats = []                                  

# cats: list of all the UNIQUE categories of the product.
    for i in range(len(prod)):
        if prod[i].category not in cats:
            cats.append(prod[i].category)

# allProds: it is list of list of products category wise
    allProds = []
    for j in cats:
        product = Product.objects.filter(category = j)

# number of products of some category       # number of slides for product of some category
        n = len(product)                                        
        nSlides = n//4 + ceil(n/4 - n//4)                       
        allProds.append([product , range(1, nSlides) , nSlides])

    params = {'allProds': allProds}
    return render(request, 'shop/index.html' , params)


def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")


