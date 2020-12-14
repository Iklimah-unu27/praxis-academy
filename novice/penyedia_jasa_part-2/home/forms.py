from django import forms
from .models import dataguru

class imgform(forms.ModelForm):
    class Meta():
         model = dataguru
         fields = ('img',)