from django.contrib import admin

from .models import Book, Course
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ['course', 'title', 'file', 'uploaded']
	list_editable = ['title', 'file']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	ordering = ('name',)