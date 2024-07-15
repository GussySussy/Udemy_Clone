from django.urls import path
from . import views

app_name = "instructor"
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('course/<uuid:pk>/', views.Course_edit.as_view(), name='course')
]