# Generated by Django 5.1.2 on 2024-11-07 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=13)),
                ('published_date', models.DateField()),
                ('description', models.TextField()),
                ('pdf', models.FileField(upload_to='books/pdfs/')),
                ('image', models.ImageField(upload_to='books/images/')),
            ],
        ),
    ]
