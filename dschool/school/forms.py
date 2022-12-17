from dataclasses import fields
from .models import Ticket
from django.forms import ModelForm, TextInput, Textarea, Select, URLInput
from django import forms


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['first_name', 'last_name', 'mail', 'address', 'address_autoschool', 'category', 'group'] 

        widgets = {
            "first_name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Имя" 
            }), 

            "last_name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Фамилия" 
            }),

            "mail": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Email" 
            }),

             "address": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите адрес"
            }), 

            "address_autoschool": Select(attrs={
                "class": "form-control",
                "placeholder": "Выберите адрес автошколы",
                "for": "Выберите адрес автошколы"
            }), 

            "category": Select(attrs={
                "class": "form-control",
                "placeholder": "Выберите категорию"
             }),

            "group": Select(attrs={
                "class": "form-control",
                "placeholder": "Выберите группу"
            })
        }
        