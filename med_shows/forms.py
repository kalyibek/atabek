from django import forms
from . import models


class ShowForm(forms.ModelForm):
    class Meta:
        model = models.MedicalShows
        fields = '__all__'
