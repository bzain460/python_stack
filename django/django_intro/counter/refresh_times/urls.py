from django.urls import path
from . import views

urlpatterns = [
    path('', views.refresh),
    path('destroy_session',views.destroy),
]