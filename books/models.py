from django.db import models
from django.utils.translation import gettext as _

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=17)  
    published_date = models.DateField(_("Date"))
    description = models.TextField()
    pdf = models.FileField(upload_to='books/pdfs/')
    image = models.ImageField(upload_to='books/images/')

    
