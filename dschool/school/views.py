from django.shortcuts import render
from .models import FAQS, Cards, Extreme


def index(request):  # функция инициализации html файла в качестве страницы
    array = ["1", "2"] # массив для ограничения проверки в одной из страниц
    cards = Cards.objects.all() # выбор всех элементов из таблицы Cards
    extreme = Extreme.objects.all()  # выбор всех элементов из таблицы Extreme
    context = {
        "cards": cards, 
        "extreme": extreme,
        "array": array,
        }                   # список инициализации элементов таблиц из бд на страничку
    return render (request, 'school/index.html', context) # функция возвращает html файл и список указанный выше

def charter(request):
    return render (request, 'school/charter.html')

def faq(request):
    faqs = FAQS.objects.all()
    return render (request, 'school/faqs.html', {"faqs": faqs})

def contacts(request):
    return render (request, 'school/contacts.html')
    
def prez(request):
    return render (request, 'school/prez.html')
  

