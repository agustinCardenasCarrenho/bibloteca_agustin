from django.urls import path
from . import views 

urlpatterns = [
    path('bibloteca/<int:status_id>' , views.bookList , name='bibloteca')
]
