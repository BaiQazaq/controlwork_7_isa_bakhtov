from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator#, EmailValidator
from django.forms import widgets

from webapp.models import Record

    
class RecordForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=256,
        label='Почта',
        required=True,
        validators=(
            MaxLengthValidator(limit_value=256),)
            #EmailValidator(whitelist = ['mail.ru', 'gmail.com', 'rambler.com', 'yahoo.com']))
    )
    author = forms.CharField(
        max_length=50,
        required=True,
        label='Автор',
        validators=(
            MinLengthValidator(limit_value=2),
            MaxLengthValidator(limit_value=50),)
        )
    text = forms.CharField(
        max_length=2000,
        required=True,
        label='Текст',
        widget=widgets.Textarea,
        validators=(
            MinLengthValidator(limit_value=2),)
        )
    
    class Meta:
        model = Record
        fields = ('author', 'email', 'text')
      
        
class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Find')
    