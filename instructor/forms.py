from django import forms
from courses.models import *
from django.forms import inlineformset_factory


class CourseForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(
            attrs={"class": "form-control", "placeholder": "Select a category"}
        ),
    )

    class Meta:
        model = Course
        fields = ["title", "subtitle", "category", "language", "price", "thumbnail"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "text",
                }
            ),
            "subtitle": forms.Textarea(
                attrs={"class": "form-control", "type": "text", "rows": "3"}
            ),
            "language": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "text",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "type": "number",
                }
            ),
            "thumbnail": forms.FileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ["title", "description"]


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ["title", "content", "video", "order"]


ChapterFormSet = inlineformset_factory(
    Section, Chapter, form=ChapterForm, extra=1, can_order=True, can_delete=True
)
