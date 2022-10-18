from django.db import models



class Book(models.Model):
    name = models.CharField(max_length=200, default='')
    author = models.CharField(max_length=200, default='')
    img = models.FileField(upload_to='books/images', default='books/images/img_not_found.png')
    description = models.CharField(max_length=1000, default='')

    likes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.author) + ": " + str(self.name)
