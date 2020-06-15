from django import forms
from .models import Maison, Personne

class MaisonForm(forms.ModelForm):
    class Meta:
        model=Maison
        fields = '__all__'

class PersonneForm(forms.ModelForm):
    class Meta:
        model=Personne
        fields='__all__'