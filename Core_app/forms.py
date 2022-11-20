from django import forms
from allauth.account.forms import LoginForm

from .models import Dia

class DiaForm(forms.ModelForm):
    class Meta:
        model = Dia
        fields = '__all__'#("",)


class MyCustomLoginForm(LoginForm):
    def login(self, *args, **kwargs):
        return super(MyCustomLoginForm, self).login(*args, **kwargs)