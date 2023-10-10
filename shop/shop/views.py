from django.shortcuts import render,redirect
from products.models import *
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.contrib.auth.models import User
from cart.cart import Cart
from django.contrib.auth.decorators import login_required


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



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        
        contact = Contact (
            name=name,
            email=email,
            subject = subject,
            message = message,
            
        )
        subject = subject 
        message  = message 
        email_from = settings.EMAIL_HOST_USER 
        try:
            print("aksckjladncjansdcjkasndcj")
            send_mail(subject,message,email_from,['almasyaseen18@gmail.com'])
            contact.save()
            return redirect('home')
        except Exception as e:
            print("sdfvsdfvsdfvsdfvssdfvsdfvsdfvdfvdf",e)
            return redirect('home')
            
            
        
        
        
    return render(request,'main/contact.html')





def register(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        customer = User.objects.create_user(username,email,password1)
        customer.first_name = firstname 
        customer.last_name = lastname
        customer.save()
        
        return redirect('register')
    return render(request,'registration/auth.html')



def user_login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            print("error here")
            return redirect('login')
            
            
    
    return render(request,'registration/auth.html')

def user_logout(request):
    logout(request)
    
    
    return redirect('home')


@login_required(login_url="/login/")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')
    




@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


def checkout(request):
    return render(request,'cart/checkout.html')



def place_order(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        print("here is the ",firstname)
        
    
    return render(request,'cart/place_order.html')