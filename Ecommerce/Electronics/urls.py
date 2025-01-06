from django.urls import path
from . import views

urlpatterns = [
    path('', views.elecs_list, name='ele-data'),
    path('add/', views.elecs_add, name='ele-add'),
    path('<int:pk>/edit/', views.elecs_edit, name='ele-edit'),
    path('<int:pk>/delete/', views.elecs_delete, name='ele-delete'),
]
