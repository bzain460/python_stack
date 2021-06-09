from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('dojo_process', views.dojo_process),
    path('ninja_process', views.ninja_process),
    path('delete', views.delete),
]