from django.forms import ModelForm
from django import forms
from home.models import dataguru, datamurid

class FormGuru(ModelForm):
    class Meta:
        model = dataguru
        fields =('nama', 'alamat','nohp','biaya','usia',)

class FormMurid(ModelForm):
    class Meta:
        model = datamurid
        fields ="__all__"