from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'Core_app'

urlpatterns = [
    path('',login_required(views.HomeTemplateView.as_view()))
]
