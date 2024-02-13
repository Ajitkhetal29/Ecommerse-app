from django.shortcuts import render, redirect , HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.views import PasswordResetConfirmView 
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm 
from .forms import ProfileUpdateForm , ReviewForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from Product.models import Product
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required


from django.contrib import messages

# Create your views here.

# sign Up
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            subject = 'Welcome to Emart !!!'
            message = f' Hii {username} we are happy to have you on Emart. Please enjoy your stay !'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail (subject , message , from_email , recipient_list , fail_silently= False)
            user = form.save()
            messages.success(request, 'Registeration Successfull!')
            return redirect('User:login_view')  # Redirect to login page after registration
    else:
        form = UserRegistrationForm()
    return render(request, 'User/register.html', {'form': form})


# Login 
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfull!')
            # Redirect to a success page or home page after login
            return redirect('Product:index')  # Replace 'home' with your home URL name
        else:
            messages.error(request, 'Invalid username or password')

    # If it's a GET request or authentication failed, show the login form
    return render(request, 'User/login.html')  # 

# reset password
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'User/password_reset_confirm.html'

# reset password
def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                use_https=request.is_secure(),
                email_template_name='User/password_reset_email.html',
            )
        return render(request, 'User/password_reset_done.html')
    else:
        form = PasswordResetForm()
    return render(request, 'User/password_reset_request.html', {'form': form})

# logout view
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Logout Successfull!')
    return redirect('User:login_view')


# profile view
@login_required
def profile(request):
    return render (request,'User/profile.html')

# update profile
def update_profile(request):
    profile = request.user.profile  # Assuming a one-to-one relationship with User
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'profile updated!')
            return redirect('User:profile')  # Redirect to the profile page or wherever you want
    else:
        form = ProfileUpdateForm( instance=profile )

    return render(request, 'User/update_profile.html', {'form': form})

# contact view
def contact(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            review = request.POST['review']
            email = request.POST['email']
            subject = 'Thank You for Your Review'
            message = f'Dear {name},\n\nThank you for submitting your review:\n\n{review}\n\nBest regards,\nEmart Shop'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail (subject , message , from_email , recipient_list , fail_silently= False)
            review = form.save()
            messages.success(request, 'review Sent!')
            return redirect('User:review')
    else:
        form = ReviewForm()
    return render(request, 'User/contact.html', {'form': form})
# review
def review(request):
    reviews = Review.objects.all()
    return render(request, 'User/review.html', {'reviews': reviews})

# add to cart view
@login_required
def add_to_cart(request,id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=id)
        cart_product = cart.objects.filter(user=request.user, product=product)
        if cart_product:
             cart.objects.get(user=request.user , product=product)
             messages.success(request , "Product already added to your Cart.")
        else:
            cart.objects.create(user=request.user , product=product)
            messages.success(request , "Product added to your Cart.")
        return redirect('User:view_cart')

# view cart view
@login_required
def view_cart(request):
    if request.user.is_authenticated:
        cart_product= cart.objects.filter(user=request.user)
        total_price = sum(item.quantity * item.product.product_price for item in cart_product)
        context={
            "cart_product":cart_product,
            "total_price":total_price
        }

        return render(request, 'User/view_cart.html',context)

# remove from the cart 
@login_required
def remove_cart(request , id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=id)
        cart_prodcut = cart.objects.filter(user = request.user , product = product )
        cart_prodcut.delete()
        messages.success(request , "Product removed from cart.")
        return redirect('User:view_cart')

# for showing cart counter

def cart_item_count(request):
    if request.user.is_authenticated:
        cart_items = cart.objects.filter(user=request.user)
        cart_item_count = cart_items.count()
    else:
        cart_item_count = 0

    return {'cart_item_count': cart_item_count}

def update_quantity(request , id):
    if request.user.is_authenticated:
        cart_product = cart.objects.get(id=id , user=request.user)
        if request.method == 'POST':
            new_quantity = int(request.POST.get('quantity',1))
            
            if new_quantity>0:
                cart_product.quantity=new_quantity
                cart_product.save()
                messages.success(request,"Quantity Updated")
                return redirect('User:view_cart')
            
# views.py

def checkout(request):
    user = request.user
    cart_products = cart.objects.filter(user=user)
    total_price = sum(item.quantity * item.product.product_price for item in cart_products)

    if request.method == 'POST':
        # Process form data, update Order model, generate invoice, etc.
        order = Order.objects.create(user=user, total_price=total_price)

        for cart_product in cart_products:
            OrderItem.objects.create(order=order, product=cart_product.product, quantity=cart_product.quantity)

        # Clear the user's cart after the order is placed
        cart_products.delete()

        # Redirect to invoice or order confirmation page with the order ID
        return redirect('User:invoice_page', order_id=order.id)

    return render(request, 'User/checkout.html', {'cart_products': cart_products, 'total_price': total_price, 'user': user})

def invoice(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, 'User/invoice.html', {'order': order})


def generate_pdf(request, order_id):
    user=request.user
    order = Order.objects.get(pk=order_id)
    template_path='User/invoice_page.html'
    context = {'order':order , 'user':user}

    # rendering template with order details
    template = get_template(template_path)
    html = template.render(context)

    # creating template

    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Disposition'] = f'attachment ; filename="invoice.pdf"'

    pisa_status = pisa.CreatePDF(html , dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>'+ html + '</pre>')
    return response


