from django.shortcuts import render
from .models import FAQS, Cards, Extreme


def index(request):
    cards = Cards.objects.all()
    extreme = Extreme.objects.all()
    return render (request, 'school/index.html', {"cards": cards, "extreme": extreme})

def charter(request):
    return render (request, 'school/charter.html')

def faq(request):
    faqs = FAQS.objects.all()
    return render (request, 'school/faqs.html', {"faqs": faqs})

def contacts(request):
    return render (request, 'school/contacts.html')


