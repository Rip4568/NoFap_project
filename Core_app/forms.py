from django import forms

from .models import Dia

class DiaForm(forms.ModelForm):
    class Meta:
        model = Dia
        fields = '__all__'#("",)