from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request, 'password/home.html')


def password(request):
    thispassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQERSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()?{}|\:;<>/'))
    len = int(request.GET.get('len'))
    for i in range(len):
        thispassword += random.choice(characters)
    return render(request, 'password/password.html', {'password': thispassword})


def about(request):
    return render(request, 'password/about.html')
