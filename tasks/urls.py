from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('login/', views.user_login, name='login'),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    path('delete/<str:pk>/' ,views.deleteTask, name='delete'),
]