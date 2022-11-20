from django.contrib.auth.decorators import login_required,permission_required
from django.urls import path

from . import views

app_name = 'Core_app'

urlpatterns = [
    path('',login_required(views.HomeTemplateView.as_view()), name='home'),
    path('att',views.alterar_variavel, name='alterar'),
]
