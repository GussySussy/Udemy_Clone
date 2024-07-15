from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_name>', views.category_view, name='category'),
]