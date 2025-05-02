from django.shortcuts import render, HttpResponse
from django.http import request

# Create your views here.

def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')