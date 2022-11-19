from django.shortcuts import render
from django.views.generic import TemplateView


""" 
    get_or_create(user, setembro)
"""
class HomeTemplateView(TemplateView):
    template_name = "Core_app/index.html"
