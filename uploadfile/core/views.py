from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
import pandas as pd
import io
import csv

from .forms import BookForm
from .models import Book


# Create your views here.
class Home(TemplateView):
    template_name = 'core/home.html'
    # return render(request, template_name)


def upload(request, **kwargs):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['myFile']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)

        uploaded_file.seek(0)
        if uploaded_file:
            df = pd.read_csv(uploaded_file, encoding='utf-8')
            # print(df.head())
            # print(df.columns)

            # render DataFrame as html
            html_table = df.to_html(classes='table table-striped table-bordered table-hover table-sm')
            context['html_table'] = html_table

    return render(request, 'core/upload.html', context)


def book_list(request):
    books = Book.objects.all()
    return render(request, 'core/book_list.html', {'books': books})


def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'core/upload_book.html', {'form': form})


def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')


