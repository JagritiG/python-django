# Register your models here.
from django.contrib import admin
from .models import Book, Csv

admin.site.register(Book)
admin.site.register(Csv)
