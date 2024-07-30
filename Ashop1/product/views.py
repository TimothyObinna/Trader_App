from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Category, Product, Productimage
# from .forms import CategoryForm, ProductForm, ProductimageForm

# Create your views here.

class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        # form = CategoryForm()
        return render(request, 'category_list.html', {'categories': categories})

    def post(self, request):
        # form = CategoryForm(request.POST, request.FILES)
        # if form.is_valid():
        #     form.save()
        #     return redirect('cat_list')
        return render(request, 'category_list.html', {'categories': Category.objects.all()})




class ProductView(View):
    def get(self, request):
        products = Product.objects.all(product_status='approved')
        # form = ProductForm()
        return render(request, 'product_list.html', {'products': products})

    def post(self, request):
        # form = ProductForm(request.POST, request.FILES)
        # if form.is_valid():
        #     form.save()
        #     return redirect('pro_list')
        return render(request, 'product_list.html', {'products': Product.objects.all()})




class ProductimageView(View):
    def get(self, request):
        product_images = Productimage.objects.all()
        # form = ProductimageForm()
        return render(request, 'productimage_list.html', {'product_images': product_images})

    def post(self, request):
        # form = ProductimageForm(request.POST, request.FILES)
        # if form.is_valid():
        #     form.save()
        #     return redirect('proimage_list')
        return render(request, 'productimage_list.html', {'product_images': Productimage.objects.all()})