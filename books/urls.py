from django.urls import path
from .views import ListBook, DetailBook, CourseList

urlpatterns = [
	path('<int:pk>/', DetailBook.as_view()),
	path('', ListBook.as_view()),
	path('courses/', CourseList.as_view()),
]