from django.urls import path
from . import views

urlpatterns = [
    path('', views.book),
    path('add_new_book', views.add_new_book),
    path('authors', views.author),
    path('add_new_author', views.add_new_author),
    path('books/<int:id>', views.books_details),
    path('authors/<int:id>', views.authors_details),
    path('add_auth/<int:id>', views.add_author),
    path('add_newbook/<int:id>', views.add_book),
]