from django import forms
from .models import Document


class UploadFileForm(forms.Form):
    file = forms.FileField()