from rest_framework import serializers
from .models import Course, Book

class CourseSerializer(serializers.ModelSerializer):
	"""docstring for CourseSerializer"""
	class Meta:
		model = Course
		fields = ['pk', 'name',]

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ['course', 'title', 'file', 'uploaded',]