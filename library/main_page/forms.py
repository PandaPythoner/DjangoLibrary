from django import forms
from .models import Book
import random
import string


def get_random_string(characters = 40):
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = characters))    
    return ran


class AddBookForm(forms.Form):
    name = forms.CharField(max_length=200)
    author = forms.CharField(max_length=200)
    img = forms.FileField()
    description = forms.CharField(max_length=1000)

    def add_book(self):
        data = self.cleaned_data
        f = self.files['img']
        img_file_name = 'books/images/' + f.name
        with open('media/' + img_file_name, 'wb+') as dest:
            for chunk in f.chunks():
                dest.write(chunk)
        new_book = Book(name=data['name'], author=data['author'], img=img_file_name, description=data['description'])
        new_book.save()


class DeleteBookForm(forms.Form):
    book_id = forms.IntegerField(required=True)


    def delete_book(self):
        data = self.cleaned_data
        book_id = int(data["book_id"])
        book = Book.objects.get(id=book_id)
        book.delete()