
from .models import cart

# for showing cart counter

def cart_item_count(request):
    if request.user.is_authenticated:
        cart_items = cart.objects.filter(user=request.user)
        cart_item_count = cart_items.count()
    else:
        cart_item_count = 0

    return {'cart_item_count': cart_item_count}