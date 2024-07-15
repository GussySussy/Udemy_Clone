from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import *
from courses.models import Course
from django.views import View


# Create your views here.
class Home(View):
    template_name = "instructor/home.html"

    def get(self, request):
        form = CourseForm()
        return render(request,self.template_name, {"form": form})
    
    def post(self,request):
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save()
            return redirect("instructor:course", pk=course.pk)
        return render(request, "instructor/home.html", {"form": form})

class Course_edit(View):
    context = {}
    form = SectionForm
    
    def get(self,request,pk):
        course = get_object_or_404(Course, pk=pk)
        self.context['course'] = course
        self.context['form'] = self.form
        return render(request, "instructor/course_edit.html", self.context)
    
    def post(self,request,pk):
        course = get_object_or_404(Course, pk=pk)
