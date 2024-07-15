from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('login', views.login, name='login'),
    path('sign-up', views.signUp, name='sign_up'),
    path('logout', views.logout, name="logout")
]