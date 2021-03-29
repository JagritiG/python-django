from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
import pandas as pd
from plotly.offline import plot
import plotly.graph_objects as go
import time


from .forms import BookForm, UploadCsvForm
from .models import Book, Csv


# Create your views here.
class Home(TemplateView):
    template_name = 'core/index.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        form = UploadCsvForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        time.sleep(2)
        get_objects = Csv.objects.latest('title')
        uploaded_file = get_objects.csv
        context['form'] = form
        context['get_objects'] = get_objects

        # render csv data
        uploaded_file.seek(0)
        if uploaded_file:
            df = pd.read_csv(uploaded_file, encoding='utf-8')

            # render DataFrame as html
            html_table = df.to_html(classes='table table-striped table-bordered table-hover table-sm')
            context['html_table'] = html_table

    else:
        form = UploadCsvForm()
        context['form'] = form

    return render(request, 'core/upload.html', context)


def delete_csv(request, pk):
    if request.method == 'POST':
        csv = Csv.objects.get(pk=pk)
        csv.delete()
    return redirect('upload')


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


def data_process(request):
    context = {}
    process = request.POST.get('Process', None)
    context['process'] = process
    return render(request, 'core/data_process.html', context)


def data_visualize(request):
    context = {}
    plots = request.POST.get('Plot', None)
    context['plots'] = plots

    get_objects = Csv.objects.latest('title')
    uploaded_file = get_objects.csv
    context['get_objects'] = get_objects

    df = pd.read_csv(uploaded_file, encoding='utf-8')
    col_list = df.columns.to_list()
    context['columns'] = col_list

    return render(request, 'core/data_visualize.html', context)


def chart(request):
    context = {}
    chart_type = request.POST.get('chart-type')
    x_var = request.POST.get('x-var')
    y_var = request.POST.get('y-var')

    # retrieve dataframe
    get_objects = Csv.objects.latest('title')
    uploaded_file = get_objects.csv
    df = pd.read_csv(uploaded_file, encoding='utf-8')

    # Plot bar chart
    if chart_type == "Bar":
        x = df[x_var]
        y = df[y_var]
        fig = go.Figure()
        bar_chart = go.Bar(x=x, y=y)
        fig.add_trace(bar_chart)

        fig.update_layout(title_text=get_objects.title)
        fig.update_xaxes(title_text=x_var)
        fig.update_yaxes(title_text=y_var)

        plot_div = plot(fig, output_type='div')
        context['plot_div'] = plot_div

    # Scatter Plot
    if chart_type == "Scatter":
        x = df[x_var]
        y = df[y_var]
        fig = go.Figure()
        scatter_plot = go.Scatter(x=x, y=y, mode='markers')
        fig.add_trace(scatter_plot)

        fig.update_layout(title_text=get_objects.title)
        fig.update_xaxes(title_text=x_var)
        fig.update_yaxes(title_text=y_var)

        plot_div = plot(fig, output_type='div')
        context['plot_div'] = plot_div

    # Scatter Plot
    if chart_type == "Histogram":
        if x_var and y_var is None:
            x = df[x_var]
            fig = go.Figure()
            hist_plot = go.Histogram(x=x, histnorm='probability')
            fig.add_trace(hist_plot)

            fig.update_layout(title_text=get_objects.title)
            fig.update_xaxes(title_text=x_var)
            plot_div = plot(fig, output_type='div')
            context['plot_div'] = plot_div

        if y_var and x_var is None:
            y = df[y_var]
            fig = go.Figure()
            hist_plot = go.Histogram(y=y, histnorm='probability')
            fig.add_trace(hist_plot)

            fig.update_layout(title_text=get_objects.title)
            fig.update_yaxes(title_text=y_var)
            plot_div = plot(fig, output_type='div')
            context['plot_div'] = plot_div

    return render(request, 'core/chart.html', context)


def dashboard(request):
    context = {}
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
    # return redirect('book_list')
    return render(request, 'core/dashboard.html', context)
