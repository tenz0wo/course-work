from django.shortcuts import render
from .models import FAQS, Cards, Extreme


def index(request):
    array = ["1", "2"]
    cards = Cards.objects.all()
    extreme = Extreme.objects.all()
    context = {
        "cards": cards, 
        "extreme": extreme,
        "array": array,
        }
    return render (request, 'school/index.html', context)

def charter(request):
    return render (request, 'school/charter.html')

def faq(request):
    faqs = FAQS.objects.all()
    return render (request, 'school/faqs.html', {"faqs": faqs})

def contacts(request):
    return render (request, 'school/contacts.html')


