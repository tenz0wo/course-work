from urllib import request
from django.shortcuts import render
import requests

def index(request):
    return render(request, 'school/index.html')