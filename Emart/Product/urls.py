from . import views
from django.urls import path
app_name = 'Product'

urlpatterns = [
    path('',views.index , name='index'),    # homepage
    path('men_fashion/',views.men_fashion , name='men_fashion'),        # men fashion page
    path('women_fashion/',views.women_fashion , name='women_fashion'),  # women fashion page
    path('electricals/',views.electrical , name='electrical'),          # electricals page
    path('toys/',views.toys , name='toys'),                             # toys page
    path('men_tshirt/',views.men_tshirt , name='men_tshirt'),           # men-tshirt page
    path('men_shirt/',views.men_shirt , name='men_shirt'),              # men -shirt page
    path('men_pants/',views.men_pants , name='men_pants'),              #men - pants page
    path('men_shoes/',views.men_shoes , name='men_shoes'),              #men -shoes page
    path('women_tshirts/',views.women_tshirts , name='women_tshirts'),  #women tshirt page
    path('women_saree/',views.women_saree , name='women_saree'),        #womrn saree page
    path('women_pants/',views.women_pants , name='women_pants'),        #women pants page
    path('women_shoes/',views.women_shoes, name='women_shoes'),         #women sohes page
    path('mobile/',views.mobile, name='mobile'),                        #mobile page
    path('laptop/',views.laptop, name='laptop'),                        #laptop page
    path('tv/',views.tv, name='tv'),                                    #tv page
    path('add/',views.add_product,name='add_product'),                  #add product page
    path('update/<int:id>',views.update_product,name='update_product'), #update product page
    path('delete/<int:id>',views.delete_product,name='delete_product'),   #delete product page
    path('rate/<int:id>',views.rate_product,name='rate_product'),   #rate product page



]
