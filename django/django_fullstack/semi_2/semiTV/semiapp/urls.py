from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('show/<int:id>', views.show),
    path('show/<int:id>/edit', views.edit),
    path('show/<int:id>/editprocess', views.editprocess),
    path('allshows',views.allshows),
    path('delete/<int:id>', views.delete)
]