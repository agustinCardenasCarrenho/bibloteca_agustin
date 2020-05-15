from django.urls import path
from django.contrib.auth.views import logout_then_login
from . import views 

urlpatterns = [
    path('' , views.home , name="home"),
    path('bibloteca/<int:status_id>' , views.bookList , name='bibloteca'),
    path('book/update/<int:book_id>/<int:state>' , views.updateBookState , name='updatebookstate'),
    path('book/update/bookprogress' , views.updateBookProgress , name="updatebookprogress"),
    path('accounts/login/' , views.login, name="login"),
    path('logout/' , logout_then_login , name='logout')
]
