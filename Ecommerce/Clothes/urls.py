from django.urls import path
from . import views

urlpatterns = [
    path('', views.clothes_list, name='cloth-data'),
    path('add/', views.clothes_add, name='cloth-add'),
    path('<int:pk>/edit/', views.clothes_edit, name='cloth-edit'),
    path('<int:pk>/delete/', views.clothes_delete, name='cloth-delete'),
]
