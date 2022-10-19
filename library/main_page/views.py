from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound
from .models import Book

# Create your views here.
def index(request):
    a = Book.objects.all().order_by("-likes")
    context = {"books": [x for x in a]}
    return render(request, "main_page/index.html", context)


# @csrf_exempt
def like_book(request):
    # print(request.POST)
    if request.method == "POST" and "book_id" in request.POST and "likes_cnt" in request.POST:
        book_id = request.POST["book_id"]
        likes_cnt = request.POST["likes_cnt"]
        # print(likes_cnt)
        if book_id.isdigit() and len(likes_cnt) > 0 and (likes_cnt[0].isdigit() or likes_cnt[0] == '-') and (len(likes_cnt) == 1 or likes_cnt[1:].isdigit()):
            book_id = int(book_id)
            likes_cnt = int(likes_cnt)
            if -1 <= likes_cnt and likes_cnt <= 1:
                book = Book.objects.get(id=book_id)
                book.likes += likes_cnt
                book.save()
            return HttpResponse(str(book.likes))
    return HttpResponse("Bad request")


def book_info_index(request):
    if not (request.method == 'GET' and 'book_id' in request.GET and request.GET['book_id'].isdigit()):
        return HttpResponseNotFound()
        
    book_id = int(request.GET['book_id'])
    book = Book.objects.get(id=book_id)
    return render(request, "main_page/book_info/index.html", context={'book': book})