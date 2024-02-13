from django import forms
from .models import Product , Rating

# form for adding more products
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_category', 'product_sub_category', 'product_brand','product_price',]
    product_image = forms.ImageField(required=False)

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['stars']

class PriceFilterForm(forms.Form):
    min_price = forms.DecimalField(label='Min ' , required=False ,)
    max_price = forms.DecimalField(label='Max ' , required=False)

