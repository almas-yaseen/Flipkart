from django.contrib import admin
from .models import *
class ImagesTublerinline(admin.TabularInline):
    model = Images

class TagTublerinline(admin.TabularInline):
    model = Tag
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesTublerinline,TagTublerinline]
    
    
    


# Register your models here.
admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_price)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images)
admin.site.register(Tag)
