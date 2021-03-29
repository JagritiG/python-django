from django import forms
from .models import Book, Csv
import pandas as pd


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'pdf', 'cover')


class UploadCsvForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ('title', 'csv')


# class ChartForm(forms.Form):
#
#     # create list of charts
#     chart = forms.ChoiceField(label='Select Chart', choices=[('Bar Chart', 'Bar Chart'), ('Histogram', 'Histogram'), ('Scatter Plot', 'Scatter Plot')])
#
#     # select x and y variables
#     get_objects = Csv.objects.latest('title')
#     uploaded_file = get_objects.csv
#     my_list = []
#     if uploaded_file:
#         df = pd.read_csv(uploaded_file, encoding='utf-8')
#         columns = list(df.columns)
#
#         for e in columns:
#             my_list.append(tuple([str(e), str(e)]))
#
#     x = forms.ChoiceField(label='Variable x', choices=my_list)
#     y = forms.ChoiceField(label='Variable y', choices=my_list)

