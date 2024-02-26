from django.shortcuts import render

def home(request):
    return render(request, 'authenticate/home.html', {})

def login(request):
    return render(request, 'authenticate/login.html', {})

