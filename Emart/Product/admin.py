from typing import Any
from django.contrib import admin
from Product.models import Product , Rating

# Register your models here.

class ProductPriceFilter(admin.SimpleListFilter):
    title='Price'
    parameter_name='product_price'
    def lookups(self, request, model_admin ):
        return (("low_price","Filter by low price(<400)"),
                ("high_price","filter by high price(>400)"))
    
    def queryset(self,request,queryset):
        if self.value()=="low_price":
            return queryset.filter(product_price__lte=400)
        elif self.value()== "high_price":
            return queryset.filter(product_price__gt=400)
        else:
            return queryset.all()
        

class ProductAdmin(admin.ModelAdmin):
    list_display=["product_name","product_category","product_sub_category","product_brand","product_price"]
    list_filter=["product_category","product_sub_category",ProductPriceFilter]
admin.site.register(Product,ProductAdmin)
admin.site.register(Rating)