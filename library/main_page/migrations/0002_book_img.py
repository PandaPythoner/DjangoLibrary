# Generated by Django 4.1.1 on 2022-09-27 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='img',
            field=models.FileField(default='books/images/img_not_found.png', upload_to='books/images'),
        ),
    ]
