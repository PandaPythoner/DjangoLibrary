from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('like_book/', views.like_book, name='like_book'),
    path('book_info/', views.book_info_index, name='book_info_index'),
    path('add_book/', views.AddBookView.as_view(), name='add_book'),
    path('delete_book/', views.DeleteBookView.as_view(), name='delete_book'),
]