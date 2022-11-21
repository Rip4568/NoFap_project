from django import template

register = template.Library()

@register.filter
def equal(valor1, valor2):
  return valor1 == valor2

@register.filter
def login_form_control(field):
  return field.as_widget(attrs={'class':'form-control','id':'form1'})

@register.filter
def email_form_control(field):
  return field.as_widget(attrs={'class':'form-control','id':'form2'})

@register.filter
def form_check_input(field):
  return field.as_widget(
    attrs={
        'id':'checkbox',
        'class':'form-check-input',
        'value':'',
        'checked':'',
    }
  )

@register.filter
def password_form_control(field):
  return field.as_widget(attrs={'id':'passwordForm','class':'form-control'})

@register.filter
def password2_form_control(field):
  return field.as_widget(attrs={id:'passworForm2', 'class':'form-control'})