from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('charter', views.charter, name='charter'),
    path('faq', views.faq, name='faq'),
    path('contacts', views.contacts, name='contacts'),
]
