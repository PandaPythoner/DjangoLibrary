from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound
from .models import Book
from .forms import AddBookForm, DeleteBookForm
from django.views.generic.edit import FormView
from django.views.generic import View


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


class AddBookView(View):
    template = "main_page/add_book/index.html"


    def get(self, request, *args, **kwargs):
        initial = None
        form = AddBookForm(initial=initial)
        context = {'form': form}
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        initial = None
        form = AddBookForm(initial=initial, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.add_book()
            return redirect("/home/")
        return render(request, self.template, {'form': form})


class DeleteBookView(View):
    template = "main_page/delete_book/index.html"


    def get_book(self, book_id):
        book_id_is_correct = True
        if not book_id.isdigit():
            book_id_is_correct = False
        else:
            book_id = int(book_id)
            book = Book.objects.filter(id=book_id)
            if not book.exists():
                book_id_is_correct = False
        return (book_id_is_correct, book_id, book[0])
        


    def get(self, request, *args, **kwargs):
        book_id = None
        book_id_is_correct = True
        book = None
        if "book_id" not in request.GET:
            book_id_is_correct = False
        else:
            book_id = request.GET["book_id"]
            book_id_is_correct, book_id, book = self.get_book(book_id)
        if not book_id_is_correct:
            return HttpResponseNotFound("Can't delete book: book_id is not correct")
        initial = {}
        initial["book_id"] = str(book_id)
        form = DeleteBookForm(initial=initial)
        context = {'form': form, 'book_id': book_id, 'book': book}
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        book_id = None
        book_id_is_correct = True
        book = None
        if "book_id" not in request.POST:
            book_id_is_correct = False
        else:
            book_id = request.POST["book_id"]
            book_id_is_correct, book_id, book = self.get_book(book_id)
        if not book_id_is_correct:
            return HttpResponseNotFound("Can't delete book: book_id is not correct")
        form = DeleteBookForm(initial=None, data=request.POST)
        print(request.POST)
        if form.is_valid():
            form.delete_book()
            return redirect("/home/")
        return render(request, self.template, {'form': form})