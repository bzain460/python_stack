from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('reglog', views.reglog),
    path('logout', views.logout),
    path('thoughts', views.thoughts),
    path('add_thought', views.add_thought),
    path('thoughts/<int:id>', views.view),
    path('like_unlike/<int:id>', views.like_unlike),
    path('del_thought/<int:id>', views.del_thought),
]