from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Create your views here.

def product(request):
    product = Product.objects.all()
    return render(request, "core/home.html", {'product':product})

def category(request, category_id):
	category = get_object_or_404(Category, id=category_id)
	return render(request, "product/category.html", {'category':category})