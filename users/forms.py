from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={
        "class": "form-control",
        "type": "email",
        "id": "email",
        "placeholder": "name@"
    }))
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "type": "password",
        "id": "password",
        "placeholder": "password"
    }))


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={
        "class": "form-control",
        "type": "email",
        "id": "email",
        "placeholder": "name@"
    }))
    password1 = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "type": "password",
        "id": "password",
        "placeholder": "password"
    }), label="Password")
    password2 = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "type": "password",
        "id": "confirm-password",
        "placeholder": "re-enter your password"
    }), label="Confirm Password")
    
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.username = self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
