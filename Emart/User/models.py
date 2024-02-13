from django.db import models
from django.contrib.auth.models import User
from Product.models import Product


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    contact = models.IntegerField()
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.TextField()
    zipcode = models.IntegerField()
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)


    def __str__(self):
        return self.user.username

# review model
class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    review = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)  # Adds the current date and time when the review is created


    def __str__(self):
        return f"Review by {self.name} on {self.date_submitted}"

#  cart Model
class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.IntegerField(Product , default=1)
    def __str__(self):
        return str(
            (
               
                self.product.product_name,
                self.user.username,
                
            )
        )

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Products=models.ManyToManyField(Product , through='OrderItem')   
    total_price = models.DecimalField(max_digits=10,decimal_places=2)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    # Add any additional fields you need for the order item.
