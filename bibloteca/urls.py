from django.urls import path
from . import views 

urlpatterns = [
    path('bibloteca/<int:status_id>' , views.bookList , name='bibloteca'),
    path('book/update/<int:book_id>/<int:state>' , views.updateBookState , name='updatebookstate'),
    path('book/update/bookprogress/<int:book_id>/<int:current_page>' , views.updateBookProgress , name="updatebookprogress")
]
