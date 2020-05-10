from django.shortcuts import render
from django.http import HttpResponse
from .models import Statu , Library , ProgressBook

def index(request):
    return render(request,'index.html' , {'user' : request.user } )

def bookList(request, status_id):
    library = Library.objects.all().filter(user = request.user.id).filter(book__statu = status_id)
    views={
        1:'leidos.html',
        2:'leyendo.html',
        3:'porleer.html'
    }
    return render(request,views.get(status_id) , { 'library' : library , 'status' : status_id} )


