from django.urls import path
from .views import index, book_translator


app_name = 'bookingTransilator'

urlpatterns = [
    path('', index, name='index'),
    path('book-translator', book_translator, name ='book_translator')
]
