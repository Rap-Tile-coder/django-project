from django.shortcuts import render

from new_app.forms import furnitureForm
from new_app.models import Furniture


# Create your views here.

def homePage(request):
    return render(request, 'view.html')

def index(request):
    return render(request, 'index.html')

def dashBoard(request):
    return render(request, 'dashboard.html')

#CRUD OPERATION : create
def furnitureData(request):
    form = furnitureForm()
    if request.method == 'POST':
        data = furnitureForm(request.POST)
        if data.is_valid():
            data.save()
    return render(request, 'form.html', {
        'form': form
    })

def furnitureDataView(request):
    data = Furniture.objects.all()
    return render(request, 'view_data.html', {'data': data})
