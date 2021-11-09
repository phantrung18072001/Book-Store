from .models import CATEGORY_CHOICES, Cart, CartItem

def add_variable_to_context(request):
    categories = CATEGORY_CHOICES
    total = 0
    count = 0
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            cart_items = CartItem.objects.filter(cart_session=cart)
            for cart_item in cart_items:
                count += 1
                total += cart_item.quantity * cart_item.book.price
        except Cart.DoesNotExist:
            cart = None
    return {
        'cart_items':cart_items,
        'categories': categories,
        'total': total,
        'count': count,
    }
