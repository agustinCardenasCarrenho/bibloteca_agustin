from django.urls import path
from django.contrib.auth.views import logout_then_login
from . import views 

urlpatterns = [
    path('' , views.home , name='home'),
    path('biblioteca/' , views.getBooks , name='getbooks'),
    path('biblioteca/<int:status_id>' , views.bookList , name='biblioteca'),
    path('book/update/<int:book_id>/<int:user_id>/<int:state>' , views.updateBookState , name='updatebookstate'),
    path('book/update/bookprogress' , views.updateBookProgress , name='updatebookprogress'),
    path('accounts/login/' , views.login, name='login'),
    path('logout/' , logout_then_login , name='logout'),
    path('books' , views.books , name='books'),
    path('book/<int:book_id>' , views.getbook , name='book'),
    path('book/buscar' , views.search_book , name='search'),
    path('book/add/<int:book_id>' , views.add_book  , name='addbook'),
    path('book/delete/<int:book_id>' , views.delete_book , name='deletebook')
]
