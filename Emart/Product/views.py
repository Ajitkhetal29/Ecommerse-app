from django.shortcuts import render , redirect
from django.http import HttpResponse
from Product.models import Product , Rating
import random
from django.contrib import messages
from .forms import ProductForm , RatingForm ,PriceFilterForm
from django.contrib.auth.decorators import login_required
from User.models import Review , cart



# Create your views here.

# product view
def index(request):
    product_list = Product.objects.all()
    all_products = list(Product.objects.all())
    random_products = random.sample(all_products, 15)
    reviews = Review.objects.all()[:3]

    context={
        'product_list':product_list,
        'random_products':random_products,
        'reviews':reviews
    }
    return render (request, 'Product/index.html',context)

# Men-fashion view
@login_required
def men_fashion(request):
    product_list = Product.objects.all()
    context={
        'product_list':product_list,
    }
    return render (request, 'Product/men-fashion.html',context)

# Women-fashion view
@login_required
def women_fashion(request):
    product_list = Product.objects.all()
    context={
        'product_list':product_list,
    }
    return render (request, 'Product/women-fashion.html',context)

# Electrical view
@login_required
def electrical(request):
    product_list = Product.objects.all()
    context={
        'product_list':product_list,
    }
    return render (request, 'Product/electricals.html',context)


# toys view
@login_required
def toys(request):
    product_list = Product.objects.all()
    form = PriceFilterForm(request.GET)
    
    if form.is_valid():
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if min_price is not None:
            product_list = product_list.filter(product_price__gte=min_price)
        if max_price is not None:
            product_list = product_list.filter(product_price__lte=max_price)


    context={
        'product_list':product_list,
        'form':form
    }
    return render (request, 'Product/toys.html',context)

# men-tshirt view
@login_required
def men_tshirt(request):
    product_list = Product.objects.all()
    form = PriceFilterForm(request.GET)
    
    if form.is_valid():
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if min_price is not None:
            product_list = product_list.filter(product_price__gte=min_price)
        if max_price is not None:
            product_list = product_list.filter(product_price__lte=max_price)


    context={
        'product_list':product_list,
        'form':form
    }
    return render (request, 'Product/men-tshirt.html',context)

# men-shirt view
@login_required
def men_shirt(request):
    product_list = Product.objects.all()
    form = PriceFilterForm(request.GET)
    
    if form.is_valid():
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if min_price is not None:
            product_list = product_list.filter(product_price__gte=min_price)
        if max_price is not None:
            product_list = product_list.filter(product_price__lte=max_price)


    context={
        'product_list':product_list,
        'form':form
    }
    return render (request, 'Product/men-shirt.html',context)


# men-pants view
@login_required
def men_pants(request):
    product_list = Product.objects.all()
    form = PriceFilterForm(request.GET)
    
    if form.is_valid():
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if min_price is not None:
            product_list = product_list.filter(product_price__gte=min_price)
        if max_price is not None:
            product_list = product_list.filter(product_price__lte=max_price)


    context={
        'product_list':product_list,
        'form':form
    }
    return render (request, 'Product/men-pants.html',context)

# men_shoes view
@login_required
def men_shoes(request):
    product_list = Product.objects.all()
    form = PriceFilterForm(request.GET)
    
    if form.is_valid():
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if min_price is not None:
            product_list = product_list.filter(product_price__gte=min_price)
        if max_price is not None:
            product_list = product_list.filter(product_price__lte=max_price)


    context={
        'product_list':product_list,
        'form':form
    }
    return render (request, 'Product/men-shoes.html',context)

# women_shoes view
@login_required
def women_tshirts(request):
    product_list = Product.objects.all()
    form = PriceFilterForm(request.GET)
    
    if form.is_valid():
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if min_price is not None:
            product_list = product_list.filter(product_price__gte=min_price)
        if max_price is not None:
            product_list = product_list.filter(product_price__lte=max_price)


    context={
        'product_list':product_list,
        'form':form
    }
    return render (request, 'Product/women-tshirts.html',context)

# women_saree view
@login_required
def women_saree(request):
    product_list = Product.objects.all()
    form = PriceFilterForm(request.GET)
    if form.is_valid():
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if min_price is not None:
            product_list = product_list.filter(product_price__gte=min_price)
        if max_price is not None:
            product_list = product_list.filter(product_price__lte=max_price)


    context={
        'product_list':product_list,
        'form':form
    }
    return render (request, 'Product/women-saree.html',context)

# women_pants view
@login_required
def women_pants(request):
    product_list = Product.objects.all()
    form = PriceFilterForm(request.GET)
    
    if form.is_valid():
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if min_price is not None:
            product_list = product_list.filter(product_price__gte=min_price)
        if max_price is not None:
            product_list = product_list.filter(product_price__lte=max_price)


    context={
        'product_list':product_list,
        'form':form
    }
    return render (request, 'Product/women-pants.html',context)


# women_shoes view
@login_required
def women_shoes(request):
    product_list = Product.objects.all()
    form = PriceFilterForm(request.GET)
    
    if form.is_valid():
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if min_price is not None:
            product_list = product_list.filter(product_price__gte=min_price)
        if max_price is not None:
            product_list = product_list.filter(product_price__lte=max_price)


    context={
        'product_list':product_list,
        'form':form
    }
    return render (request, 'Product/women-shoes.html',context)

# mobile view
@login_required
def mobile(request):
    product_list = Product.objects.all()
    form = PriceFilterForm(request.GET)
    
    if form.is_valid():
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if min_price is not None:
            product_list = product_list.filter(product_price__gte=min_price)
        if max_price is not None:
            product_list = product_list.filter(product_price__lte=max_price)


    context={
        'product_list':product_list,
        'form':form
    }
    return render (request, 'Product/mobile.html',context)

# Laptop view
@login_required
def laptop(request):
    product_list = Product.objects.all()
    form = PriceFilterForm(request.GET)
    
    if form.is_valid():
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if min_price is not None:
            product_list = product_list.filter(product_price__gte=min_price)
        if max_price is not None:
            product_list = product_list.filter(product_price__lte=max_price)


    context={
        'product_list':product_list,
        'form':form
    }
    return render (request, 'Product/laptop.html',context)

# tv view
@login_required
def tv(request):
    product_list = Product.objects.all()
    form = PriceFilterForm(request.GET)
    
    if form.is_valid():
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if min_price is not None:
            product_list = product_list.filter(product_price__gte=min_price)
        if max_price is not None:
            product_list = product_list.filter(product_price__lte=max_price)


    context={
        'product_list':product_list,
        'form':form
    }
    return render (request, 'Product/tv.html',context)

# view for adding product 
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST or None)  # Include request.FILES for file data
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added !')
            return redirect('Product:index')  # Redirect to a list view of products or any other appropriate page
    else:
        form = ProductForm()
    
    return render(request, 'Product/add-product.html', {'form':form})

# update product
@login_required
def update_product(request,id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)
    context={
        'form':form,
        'product':product
    }
    if form.is_valid():
        form.save()
        messages.success(request, 'Product updated !')
        return redirect('Product:index')
    return render(request, 'Product/update-product.html', context)

# delete product
@login_required
def delete_product(request,id):
    product = Product.objects.get(id=id)
    context = {
        'product':product
    }
    if request.method=='POST':
        product.delete()
        messages.success(request, 'Product deleted !')
        return redirect('Product:index')
    return render(request,'Product/delete-product.html',context)


def rate_product(request, id):
    product = Product.objects.get(pk=id)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.product = product
            rating.user = request.user
            rating.save()

            # Update total ratings and average rating for the product
            product.total_ratings += 1
            product.average_rating = (product.average_rating * (product.total_ratings - 1) + rating.stars) / product.total_ratings
            product.save()
            messages.success(request, 'Rating Submitted !')
            return redirect('Product:index',)
    else:
        form = RatingForm()
    return render(request, 'Product/rate_product.html', {'form': form, 'product': product})