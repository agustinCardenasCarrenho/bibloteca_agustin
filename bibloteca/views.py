from django.shortcuts import render ,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Statu , Library ,Book

def index(request):
    return render(request,'index.html' , {'user' : request.user } )

def bookList(request, status_id):
    library = Library.objects.all().filter(user = request.user.id).filter(book__statu = status_id)
    statu = Statu.objects.all()
    views={
        1:'leidos.html',
        2:'leyendo.html',
        3:'porleer.html'
    }
    return render(request,views.get(status_id) , { 'library' : library , 'status_id' : status_id , 'status' : statu } )

def updateBookState(request , book_id, state):
    Book.objects.filter(id = book_id).update(statu = state) 
    return redirect('http://localhost:8000/bibloteca/'+str(state))
    

