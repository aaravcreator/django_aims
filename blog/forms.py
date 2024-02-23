from django import forms
from .models import Author
class AuthorFilterForm(forms.Form):
    name = forms.CharField(max_length=255,required=True)

class AuthorForm(forms.ModelForm):
    class Meta:
        fields = ['name','age','email','bio']
        model = Author