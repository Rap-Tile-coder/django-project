from django.urls import path

from new_app import views

urlpatterns = [
    path('test',views.homePage, name = 'home'),
    path('', views.index, name='index'),
    path('dashboard', views.dashBoard, name="landingpage"),
    path('forms',views.furnitureData, name="forms"),
    path('dataview', views.furnitureDataView, name = "dataview"),
    path('del/<int:id>/', views.items_delete, name= 'del'),
    path('update/<int:id>/',views.itemUpdate,name= 'update')
]