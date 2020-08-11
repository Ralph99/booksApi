from django.urls import path
from .views import list_books,  book_detail
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pages'

urlpatterns = [
    path('', list_books, name='book_list'),
    path('<slug:course_slug>/', list_books, name='list_books_by_course'),
    #path('<slug:slug>/', book_detail, name='book_detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)