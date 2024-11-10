from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    published_date = forms.DateField(input_formats=['%d-%m-%Y', '%Y-%m-%d'], label="Published Date")
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'published_date', 'description', 'pdf', 'image']
