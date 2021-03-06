from django import forms
from django.forms import widgets


class GuestForm(forms.Form):
    name = forms.CharField(max_length=100, label='Имя')
    mail = forms.EmailField(max_length=100, label='Email')
    description = forms.CharField(max_length=2000, widget=widgets.Textarea, required=False,label='Текст')