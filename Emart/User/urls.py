from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import password_reset_request, CustomPasswordResetConfirmView 


app_name = 'User'
urlpatterns = [
    path('register/',views.register , name='register'),    # register
    path('login/',views.login_view , name='login_view'),    # login
    path('password_reset/', password_reset_request, name='password_reset'), #reset password
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'), #reset password
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='User/password_reset_complete.html'), name='password_reset_complete'), #reset password
    path('logout/',views.logout_view,name='logout_view'), #logout 
    path('profile/',views.profile,name='profile'),  # profile
    path('update_profile/',views.update_profile,name='update_profile'),  #update profile
    path('contact/',views.contact,name='contact'), # contact page
    path('reviews/',views.review,name='review'), # review page
    path('add_to_cart/<int:id>',views.add_to_cart , name='add_to_cart'), # add to cart view
    path('cart/',views.view_cart,name='view_cart'), # view cart
    path('remove_cart/<int:id>',views.remove_cart,name='remove_cart'), #remove from cart
    path('update_quantity/<int:id>/', views.update_quantity, name='update_quantity'),
    path('checkout/', views.checkout, name='checkout'),
    path('invoice/<int:order_id>', views.invoice, name='invoice_page'),
    path('generate_pdf/<int:order_id>',views.generate_pdf,name ='generate_pdf')


]
