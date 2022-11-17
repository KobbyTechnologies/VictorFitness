from dataclasses import fields
from select import select
from socket import fromshare
from xml.parsers.expat import model
from django.forms import ModelForm, Textarea, EmailInput, TextInput, Select
from .models import FullInfo



class FullInfo(ModelForm):
    class Meta:
        model = FullInfo
        fields = [
            'first_name',
            'last_name',
            'email',
            'adress_line_1',
            'adress_line_2',
            'city',
            'country',
            'phone',
            'gender'
        ]
        widgets = {
            'first_name': TextInput(),
            'last_name':TextInput(),
            'email':EmailInput(),
            'adress_line_1':TextInput(),
            'adress_line_2':TextInput(),
            'city': TextInput(),
            'country': Select(),
            'phone': TextInput(),
            'gender': Select()

        }