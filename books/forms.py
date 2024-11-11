from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book

class BookForm(forms.ModelForm):
    published_date = forms.DateField(input_formats=['%d-%m-%Y', '%Y-%m-%d'], label="Published Date")
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'published_date', 'description', 'pdf', 'image','available']

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
