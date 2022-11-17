from django.urls import path
from .views import *

urlpatterns = [
    path('all-books/', get_all_books),
    path('book/<str:pk>/', get_book),
    path('add-book/', add_book),
    path('update-book/<str:pk>/', update_book),
    path('delete-book/<str:pk>/', delete_book)
]
