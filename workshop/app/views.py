from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def mission_available(request):
    return render(request, 'mission_available.html')

def my_missions(request):
    return render(request, 'my_missions.html')

def map(request):
    return render(request, 'map.html')

def settings(request):
    return render(request, 'settings.html')

def partenaire(request):
    return render(request, 'partenaire.html')

def login(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration.html')

def informations(request):
    return render(request, 'informations.html')

