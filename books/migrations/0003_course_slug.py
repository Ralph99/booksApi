# Generated by Django 3.0 on 2020-08-05 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(default='course-slug', max_length=200),
        ),
    ]
