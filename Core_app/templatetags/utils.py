from django import template

register = template.Library()

def equal(valor1, valor2):
  return valor1 == valor2