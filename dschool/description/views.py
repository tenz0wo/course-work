from django.shortcuts import render
from requests import request
from .models import Info


def car(request):
    info = Info.objects.all()
    context =  {"info": info}
    return render (request, 'description/car.html', context)

def carbe(request):
    info = Info.objects.all()
    context =  {"info": info}
    return render (request, 'description/car-BE.html', context)

def moto(request):
    info = Info.objects.all()
    context =  {"info": info}
    return render (request, 'description/moto.html', context)

def motoa1(request):
    info = Info.objects.all()
    context =  {"info": info}
    return render (request, 'description/moto-A1.html', context)

def exdriving(request):
    info = Info.objects.all()
    context =  {"info": info}
    return render (request, 'description/exdriving.html' ,context)

def rally(request):
    info = Info.objects.all()
    context =  {"info": info}
    return render (request, 'description/rally.html' ,context)

def drift(request):
    info = Info.objects.all()
    context =  {"info": info}
    return render (request, 'description/drift.html' ,context)

def spec(request):
    info = Info.objects.all()
    context =  {"info": info}
    return render (request, 'description/spec.html' ,context)

def c(request):
    info = Info.objects.all()
    context =  {"info": info}
    return render (request, 'description/carC.html', context)

def c1(request):
    info = Info.objects.all()
    context =  {"info": info}
    return render (request, 'description/car-C1.html', context)