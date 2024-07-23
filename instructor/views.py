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
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save()
            return redirect("instructor:course", pk=course.pk)
        return render(request, "instructor/home.html", {"form": form})


class CourseEdit(View):
    template_name = "instructor/course_edit.html"

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        section_form = SectionForm()
        chapter_form = ChapterForm()
        context = {
            "course": course,
            "section_form": section_form,
            "chapter_form": chapter_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        if "section_submit" in request.POST:
            section_form = SectionForm(request.POST)
            chapter_form = ChapterForm()
            if section_form.is_valid():
                section = section_form.save(commit=False)
                section.course = course
                last_section = (
                    Section.objects.filter(course=course).order_by("sequence").last()
                )
                if last_section:
                    section.sequence = last_section.sequence + 1
                else:
                    section.sequence = 1
                section.save()
                section.tot_time = section.calc_time()
                section.save(update_fields=["tot_time"])
                return redirect("instructor:course_edit", pk=course.pk)
        elif "chapter_submit" in request.POST:
            section_id = request.POST.get("section_id")
            section = get_object_or_404(Section, pk=section_id)
            chapter_form = ChapterForm(request.POST, request.FILES)
            section_form = SectionForm()
            if chapter_form.is_valid():
                chapter = chapter_form.save(commit=False)
                chapter.section = section
                chapter.save()
                section.tot_time = section.calc_time()
                section.save(update_fields=["tot_time"])
                return redirect("instructor:course_edit", pk=course.pk)

        context = {
            "course": course,
            "section_form": section_form,
            "chapter_form": chapter_form,
        }
        return render(request, self.template_name, context)


class DeleteSection(View):
    def post(self, request, section_id):
        section = get_object_or_404(Section, pk=section_id)
        course_id = section.course.cid
        section.delete()
        return redirect("instructor:course_edit", pk=course_id)


class DeleteChapter(View):
    def post(self, request, chapter_id):
        chapter = get_object_or_404(Chapter, pk=chapter_id)
        section_id = chapter.section.id
        chapter.delete()
        section = get_object_or_404(Section, pk=section_id)
        section.tot_time = section.calc_time()
        section.save(update_fields=["tot_time"])
        return redirect("instructor:course_edit", pk=section.course.id)
