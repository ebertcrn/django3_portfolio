from django.shortcuts import render
import random
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'pwgenerator/home.html')

def password(request):
    characters = []

    if request.GET.get('lowercase'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('specialchars'):
        characters.extend(list('!@#$%&*'))

    length = int(request.GET.get('length', 10))  # default value = 10
    thepassword = ''

    if not len(characters):
        return render(request, 'pwgenerator/passworderror.html')
    for eachChar in range(length):
        thepassword += random.choice(characters)

    return render(request, 'pwgenerator/password.html', {'password': thepassword})