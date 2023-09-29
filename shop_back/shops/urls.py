from django.urls import path
from . import views

urlpatterns = [
    path('api/v1', views.API_View, name='apiTest'),
    path('api/v1/<int:id>/', views.API_View_D, name='apiD')
    ]