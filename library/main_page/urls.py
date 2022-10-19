from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('like_book/', views.like_book, name='like_book'),
    path('book_info', views.book_info_index, name='book_info_index')
]