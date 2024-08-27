from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'translate/index.html')

def register(request):
    return render(request, 'translate/register.html')
