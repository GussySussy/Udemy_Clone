from django.urls import path
from . import views as cart_views


urlpatterns = [
    path('', cart_views.CartView.as_view(), name='cart_index'),
    path('remove_from_cart/<uuid:course_id>/', cart_views.remove_from_cart, name='remove_from_cart'),
]