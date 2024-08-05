from django.urls import path

from new_app import views

urlpatterns = [
    path('',views.homePage, name = 'home'),
    path('index', views.index, name='index'),
    path('dashboard', views.dashBoard, name="landingpage")
]