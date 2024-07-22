from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import Cart, CartItem


@receiver(user_logged_in)
def merge_cart(sender, user, request, **kwargs):
    session_key = request.session.session_key
    if not session_key:
        return

    try:
        session_cart = Cart.objects.get(session_key=session_key)
    except Cart.DoesNotExist:
        return

    user_cart, created = Cart.objects.get_or_create(user=user)

    for item in session_cart.items.all():
        CartItem.objects.get_or_create(cart=user_cart, course=item.course)

    session_cart.delete()
