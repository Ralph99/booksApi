from django.shortcuts import render, get_object_or_404

from books.models import Book, Course

# Create your views here.

def list_books(request, course_slug=None):
	course = None
	courses = Course.objects.all()
	books = Book.objects.all()
	if course_slug:
		course = get_object_or_404(Course, slug=course_slug)
		books = books.filter(course=course)

# template and context
	template = 'pages/list_books.html'
	context = {'books':books, 'course':course, 'courses':courses,}

	return render(request, template, context)

def book_detail(request, slug):
	book = get_object_or_404(Book, slug=slug)
	return render(request, 'pages/book_detail.html', {'book':book})