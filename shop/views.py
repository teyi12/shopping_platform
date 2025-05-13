from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect
from .models import Product



def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', context={'products': products})
    

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', context={'product': product})



@staff_member_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/product_list/')
    else:
        form = ProductForm()
    return render(request, 'shop/add_product.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)  # Nur Admins oder Personal
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')  # Leitet zurück zur Produktliste

def category_list_view(request):
    categories = Category.objects.all()
    return render(request, 'shop/product_list.html', {'categories': categories})

# @staff_member_required
# def add_category(request):
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('shop:product_list')
#     else:
#         form = CategoryForm()
#     return render(request, 'shop/add_category.html', {'form': form})




# Produktliste
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

# Produktdetailansicht
def product_detail_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

