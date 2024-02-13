





from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Product model
class Product(models.Model):
    
    def __str__(self):
        return str(
            (
                self.id,
                self.product_name,
                self.product_category,
                self.product_sub_category,
               
            )
        )
    
    product_name = models.CharField(max_length=200)
    product_category = models.CharField(max_length=200)
    product_sub_category = models.CharField(max_length=200)
    product_brand = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_image = models.ImageField(upload_to='pictures/',blank=True, null=True)
    total_ratings = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0.0)

class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()
    
    def __str__(self):
        return str(
            (
                self.product.product_name,
                self.stars,
                self.user.username,               
            )
        )


