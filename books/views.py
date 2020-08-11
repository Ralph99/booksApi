from rest_framework import generics

from .models import Course, Book
from .serializers import CourseSerializer, BookSerializer

class ListBook(generics.ListAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class DetailBook(generics.RetrieveAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class CourseList(generics.ListAPIView):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer