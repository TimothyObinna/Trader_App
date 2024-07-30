from django import forms
from .models import Category, Product, Productimage

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name', 'image')



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'

        fields = ('product_id', 'product_name', 'user', 'vendor', 'image', 'description', 'category', 
                  'product_details', 'price', 'old_price', 'specification', 'product_status', 
                  'in_stock', 'featured', 'digital', 'my_stock', 'last_updated')
        


class ProductimageForm(forms.ModelForm):
    class Meta:
        model = Productimage
        fields = ('product_name', 'images')