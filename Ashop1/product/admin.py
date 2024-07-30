from django.contrib import admin
from  .models import (Category, Product, CartOrder, CartOrderItems, Productimage, ProductReview, 
                      WishList, OrderAddress)

# Register your models here.

@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ['category_id','category_name', 'category_image', 'date']  # category_image here is the image method name in the category model



class ProductImageAdmin(admin.TabularInline):
    model = Productimage

admin.site.register(Productimage)    



@admin.register(Product)
class Productadmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ['product_id','product_name', 'user', 'vendor', 'category', 'product_image', 
                    'price', 'old_price', 'product_status', 'date'] # same explained above ; this for the product model


   






