from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View

from .models import Setembro, Dia

class HomeTemplateView(View):
    template_name = "Core_app/index.html"
    
    def get(self, request, *args, **kwargs):
        setembro, created = Setembro.objects.get_or_create(usuario=self.request.user)
        if created:#se ele acabou se ser criado
            for i in range(1, 30 + 1):#execute 30x (quantidade de dias no mes de setembro)
                Dia.objects.create(mes=setembro, dia=i, estado='N')
        context = {
            'setembro':setembro,
            'dias': setembro.dias.all(),
        }
        return render(request=self.request, template_name=self.template_name,context=context)

    def post(self, request, *args, **kwargs):
        return render(request=self.request, template_name=self.template_name, context={})

def alterar_variavel(request):
    EH_SETEMBRO = not EH_SETEMBRO
    return HttpResponseRedirect(reverse('Core_app:home'))