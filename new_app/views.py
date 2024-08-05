from django.shortcuts import render

# Create your views here.

def homePage(request):
    return render(request, 'view.html')

def index(request):
    return render(request, 'index.html')

def dashBoard(request):
    return render(request, 'dashboard.html')
