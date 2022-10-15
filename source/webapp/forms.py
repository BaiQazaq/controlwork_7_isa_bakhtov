from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator
from django.forms import widgets

from webapp.models import Record

def upper_validator(string):
    if not string[0].isupper():
        raise ValidationError('First letter must be in Uppercase')
    return string
    
class RecordForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=256,
        label='Email',
        required=True,
        validators=(
            MaxLengthValidator(limit_value=256),
            EmailValidator(),)
    )
    author = forms.CharField(
        max_length=50,
        required=True,
        label='Имя',
        validators=(
            MinLengthValidator(limit_value=2),
            MaxLengthValidator(limit_value=50),
            upper_validator,)
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
    