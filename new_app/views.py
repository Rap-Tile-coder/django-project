from django.shortcuts import render, redirect

from new_app.forms import furnitureForm
from new_app.models import Furniture


# Create your views here.

def homePage(request):
    return render(request, 'view.html')

def index(request):
    return render(request, 'index.html')

def dashBoard(request):
    return render(request, 'dashboard.html')

#CRUD OPERATION : create operation
def furnitureData(request):
    form = furnitureForm()
    if request.method == 'POST':
        data = furnitureForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('')
    return render(request, 'form.html', {
        'form': form
    })

def furnitureDataView(request):
    data = Furniture.objects.all()
    return render(request, 'view_data.html', {'data': data})

#delete operation

def items_delete(request,id):
    data = Furniture.objects.get(id= id)
    data.delete()
    return redirect("dataview")


# update method

def itemUpdate(request, id):
    data =Furniture.objects.get(id= id)
    form = furnitureForm(instance=data)
    if request.method == 'POST':
        data = furnitureForm(request.POST, instance=data)
        if data.is_valid():
            data.save()
            return redirect('dataview')

    return render(request, 'detailsupdate.html', {'form': form})


