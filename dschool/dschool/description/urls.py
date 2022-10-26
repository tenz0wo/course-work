from django.urls import path
from . import views

urlpatterns = [
    path('car/', views.car, name='car'),
    path('car-BE/', views.carbe, name='car-BE'),
    path('moto/', views.moto, name='moto'),
    path('moto-A1/', views.motoa1, name='motoa1'),
    path('exdriving/', views.exdriving, name='exdriving'),
    path('rally/', views.rally, name='rally'),
    path('drift/', views.drift, name='drift'),
    path('spec/', views.spec, name='spec'),
    path('car-C/', views.c, name='c'),
    path('car-C1/', views.c1, name='c1'),

]