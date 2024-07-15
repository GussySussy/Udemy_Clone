from django import forms
from courses.models import *


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
        fields = ["sequence", "title", "description"]
        widgets = {
            "sequence": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "type": "number",
                }
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "type": "text", "rows": "3"}
            ),
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "text",
                }
            ),
        }
