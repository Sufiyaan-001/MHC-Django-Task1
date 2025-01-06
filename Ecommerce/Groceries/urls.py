from django.urls import path
from . import views

urlpatterns = [
    path('', views.groceries_list, name='grocs-data'),
    path('add/', views.groceries_add, name='grocs-add'),
    path('<int:pk>/edit/', views.groceries_edit, name='grocs-edit'),
    path('<int:pk>/delete/', views.groceries_delete, name='grocs-delete'),
]
