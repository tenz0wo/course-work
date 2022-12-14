from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), #инициализирование панели admin
    path('', include('school.urls')), #инициализирование приложения school в основную директорию 
    path('categories/', include('description.urls')), #инициализирование приложения description в основную директорию

]

