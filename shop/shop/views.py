from django.shortcuts import render,redirect
from products.models import *


def base(request):
    return render(request,'main/base.html')


def home(request):
    product = Product.objects.filter(status='publish')
    context = {
        'product':product,
    }
    return render(request,'main/index.html',context)

def product(request):
    categories = Categories.objects.all() 
    filter_price = Filter_price.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()
    CATID = request.GET.get('categories')
    PRICE = request.GET.get('price')
    COLOR = request.GET.get('colors')
    BRANDID = request.GET.get('brand')
    
    ATOZ = request.GET.get('ATOZ')
    ZTOA = request.GET.get('ATOZ')
    pricelow = request.GET.get('PRICE_LOW')
    pricehigh = request.GET.get('PRICE_HIGH')
    newitem = request.GET.get('NEW')
    olditem = request.GET.get('OLD_PRODUCT')
    
    
    
    
    if CATID:
        product = Product.objects.filter(categories=CATID,status='publish')
        
    elif PRICE:
        product = Product.objects.filter(filter_price = PRICE,status='publish')
    elif COLOR:
        product = Product.objects.filter(color=COLOR,status='publish')
     
    elif BRANDID:
        product = Product.objects.filter(brand=BRANDID,status='publish')
        
    elif pricelow:
        product = Product.objects.filter(status='publish').order_by('price')
    elif pricehigh:
         product = Product.objects.filter(status='publish').order_by('-price')
        
        
    
    elif ATOZ:
        product = Product.objects.filter(status='publish').order_by('name')
    elif ZTOA:
        product = Product.objects.filter(status='publish').order_by('-name')
        
    elif newitem:
        product = Product.objects.filter(condition='NEW'  , status='publish').order_by('-id')
    
    elif olditem:
        product = Product.objects.filter(condition='OLD'  , status='publish').order_by('-id')
        
        
            
        
    
        
        
    else:
        product = Product.objects.filter(status='publish')
    
    context = {
        'product':product,
        'categories':categories,
        'filter_price':filter_price,
        'color':color,
        'brand':brand,
    }
    return render(request,'main/product.html',context)
    


def search(request):
    query = request.GET.get('query')
    product = Product.objects.filter(name__icontains=query)
    context = {
        'product':product,
        
    }
    return render(request,'main/search.html',context)


def product_details(request,id):
    prod = Product.objects.filter(id=id).first()
    context = { 
               'prod':prod,
               }
    return render(request,'main/product_single.html',context)


