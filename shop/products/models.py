from django.db import models
from django.utils import timezone
from django.utils import timezone
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
    information = models.TextField()
    description = models.TextField()
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
    
    

            