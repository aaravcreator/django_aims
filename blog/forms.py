from django import forms
from .models import Author
class AuthorFilterForm(forms.Form):
    name = forms.CharField(max_length=255,required=True)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
class AuthorForm(forms.ModelForm):
    class Meta:
        fields = ['name','age','email','bio','photo',]
        model = Author