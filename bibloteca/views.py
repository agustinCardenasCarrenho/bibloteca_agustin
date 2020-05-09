from django.shortcuts import render
from django.http import HttpResponse
from .models import Statu , Library

def index(request, status_id):
    status = Statu.objects.all()
    library = Library.objects.all().filter(user = request.user.id).filter(book__statu = status_id)
    return render(request,'index.html' , {'user' : request.user , 'library' : library , 'status' : status_id} )
    #return HttpResponse(library)

