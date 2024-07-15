from django.shortcuts import render

from courses.models import *


def home(request):
    context = {"categories": Category.objects.all()}
    return render(request, "core/base.html", context)


def category_view(request, category_name):
    category = Category.objects.get(slug = category_name)
    context = {"category" : category, "categories" : Category.objects.all()}
    context["courses"] = category.courses.all()
    return render(request, "core/category.html", context)
