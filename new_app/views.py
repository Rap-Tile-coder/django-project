from django.shortcuts import render

from new_app.forms import furnitureForm


# Create your views here.

def homePage(request):
    return render(request, 'view.html')

def index(request):
    return render(request, 'index.html')

def dashBoard(request):
    return render(request, 'dashboard.html')

def furnitureData(request):
    form = furnitureForm()
    return render(request, 'form.html', {
        'form': form
    })
