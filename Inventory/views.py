from django.shortcuts import render

def product_list(request):
    return render(request, 'inventory/product/product-list.html')
    
def add_product(request):
    return render(request, 'inventory/product/product-add.html')


def category(request):
    return render(request, 'inventory/product/product-category.html')
    
def sub_category(request):
    return render(request, 'inventory/product/product-sub_category.html')

def brands(request):
    return render(request, 'inventory/product/product-brands.html')   

def units(request):
    return render(request, 'inventory/product/product-units.html') 
    
def sku(request):
    return render(request, 'inventory/product/product-sku.html')    