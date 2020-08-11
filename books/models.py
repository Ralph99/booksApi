from django.db import models

from django.urls import reverse

# Create your models here.

class Course(models.Model):
	name = models.CharField(max_length=30, default='General', db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)

	def __str__(self):
		return self.name

class Book(models.Model):
	course = models.ForeignKey(Course, blank=True, on_delete=models.CASCADE)
	title = models.CharField(max_length=250, blank=True)
	slug = models.SlugField(max_length=250)
	file = models.FileField(upload_to='books/%Y/%m/%d', blank=True)
	uploaded = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title