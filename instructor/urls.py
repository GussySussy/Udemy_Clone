from django.urls import path
from . import views

app_name = "instructor"
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('course/<uuid:pk>/', views.CourseEdit.as_view(), name='course_edit'),
    path('course/section/delete/<int:section_id>/', views.DeleteSection.as_view(), name='delete_section'),
    path('course/chapter/delete/<int:chapter_id>/', views.DeleteChapter.as_view(), name='delete_chapter'),
]