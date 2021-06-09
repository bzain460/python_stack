from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.hani),
    path('result',views.karmel)
]