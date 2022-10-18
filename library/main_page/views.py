from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from .models import Book

# Create your views here.
def index(request):
    a = Book.objects.all()
    context = {"books": [x for x in a]}
    return render(request, "main_page/index.html", context)


def book_info_index(request):
    if not (request.method == 'GET' and 'book_id' in request.GET and request.GET['book_id'].isnumeric()):
        return HttpResponseNotFound()
        
    book_id = int(request.GET['book_id'])
    book = Book.objects.get(id=book_id)
    return render(request, "main_page/book_info/index.html", context={'book': book})