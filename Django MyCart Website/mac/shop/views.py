from django.shortcuts import render
from django.http import HttpResponse

from .models import Product
from math import ceil
# Create your views here.
def index(request):
    # return HttpResponse('Index Shop')
    products = Product.objects.all()
    # print(products)
    # Len = len(products)
    # no_of_slides = Len//4 + ceil((Len/4-(Len//4)))
    # param = {'No_OfSlide':no_of_slides,'range':range(1,no_of_slides),'product':products}

    # allProds = [[products,range(1,no_of_slides),no_of_slides],[products,range(1,no_of_slides),no_of_slides ]]
    allProds = []
    catprdos = Product.objects.values('category','id')
    cats = {item['category'] for item in catprdos}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        Len = len(prod)
        no_of_slides = Len // 4 + ceil((Len / 4 - (Len // 4)))
        allProds.append([prod,range(1,no_of_slides),no_of_slides])


    params = {"allProds":allProds}

    return render(request,'shop/index.html',params)

def about(request):
    # return HttpResponse('shop/about.html')
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse('contact')

def tracker(request):
    return HttpResponse('tracker')

def search(request):
    return HttpResponse('search')

def prodView(request):
    return HttpResponse('prodView')

def checkout(request):
    return HttpResponse('checkout')

