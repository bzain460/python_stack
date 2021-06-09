from django.urls import path
from . import views
urlpatterns = [

    path('', views.index),
    path('dojo' ,views.add_dojo),
    path('ninjas',views.add_ninja)
]