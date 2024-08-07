from django.urls import path

from new_app import views

urlpatterns = [
    path('',views.homePage, name = 'home'),
    path('index', views.index, name='index'),
    path('dashboard', views.dashBoard, name="landingpage"),
    path('forms',views.furnitureData, name="forms"),
    path('dataview', views.furnitureDataView, name = "dataview")
]