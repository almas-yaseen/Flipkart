from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

class Brand(models.Model):
    name  = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Color(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Filter_price(models.Model):
    FILTER_PRICE = ( 
                    ('10000 TO 20000','10000 TO 20000'),
                    
                    ('20000 TO 30000' ,'20000 TO 30000' ),
                    ('30000 TO 40000' , '30000 TO 40000'),
                    ('40000 TO 50000','40000 TO 50000'),
                    ('60000 TO 70000','60000 TO 70000'),
    
                    )
    
    price = models.CharField(choices=FILTER_PRICE,max_length=100)
    def __str__(self):
        return self.price
    
    
    
class Product(models.Model):
    CONDITION = (('NEW','NEW'),('OLD','OLD'))
    STOCK = (('IN STOCK','IN STOCK'),('OUT OF STOCK','OUT OF STOCK'))
    STATUS =  ('publish','publish'),('draft','draft')
    name = models.CharField(max_length=100)
    unique_id = models.CharField(unique=True,max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to='Product_images/img')
    price = models.IntegerField()
    condition = models.CharField(choices=CONDITION,max_length=100)
    information = RichTextField(null=True)
    description = RichTextField(null=True)
    stock = models.CharField(choices=STOCK,max_length=200)
    status = models.CharField(choices=STATUS,max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    filter_price = models.ForeignKey(Filter_price,on_delete=models.CASCADE)

    
    
    def save(self,*args,**kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id = self.created_date.strftime('75%Y%m%d23') + str(self.id)
        return super().save(*args,**kwargs)
    
    def __str__(self):
        return self.name
    

class Images(models.Model):
    image = models.ImageField(upload_to='Product_images/img')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    
    

class Contact(models.Model):
    name  =  models.CharField(max_length=200)
    email  = models.EmailField(max_length=200)
    subject  = models.CharField(max_length=100)
    message  = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
    
    
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=200)
    country  =models.CharField(max_length=100)
    pincode =  models.IntegerField()
    address  = models.TextField(max_length=100)
    city  =models.CharField(max_length=100)
    state  =models.CharField(max_length=100)
    pincode = models.IntegerField() 
    phone = models.IntegerField() 
    email  = models.EmailField(max_length=100)
    additional_info = models.TextField()
    amount  = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=300,null=True,blank=True)
    paid = models.BooleanField(default=False,null=True)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Product_images/order')
    quantity = models.CharField(max_length=20)
    price = models.CharField(max_length=50)
    total = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.order.user.username
    
    
    
    
    
    
    

    
    
    