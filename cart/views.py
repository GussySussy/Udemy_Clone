from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Course, Cart, CartItem


def get_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart

def remove_from_cart(request, course_id):
    course = get_object_or_404(Course, cid=course_id)
    cart = get_cart(request)
    cart_item = get_object_or_404(CartItem, cart=cart, course=course)
    cart_item.delete()
    return redirect("cart_index")


class CartView(View):
    template_name = "cart/index.html"
    context = {}

    def get(self, request):
        cart = get_cart(request)
        return render(request, self.template_name, {"cart": cart})

    def post(self, request):
        course_id = request.POST.get("course_id")
        course = get_object_or_404(Course, cid=course_id)
        cart = get_cart(request)
        CartItem.objects.get_or_create(cart=cart, course=course)
        return redirect("cart_index")
