from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate ,login as do_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .models import Statu , Library ,Book , Progress , State 


def home(request):
    if request.user.id is None:
        return render(request ,'home.html' )
    else :
        return redirect('/biblioteca')
       

@login_required
def bookList(request, status_id):
    library = State.objects.all().filter(user = request.user.id, statu__id = status_id)
    statu = Statu.objects.all()
    views={
        1:'leidos.html',
        2:'leyendo.html',
        3:'porleer.html'
    }
    return render(request,views.get(status_id) , { 'library' : library , 'status_id' : status_id , 'status' : statu } )

@login_required
def getBooks(request):
    library = Library.objects.all().filter(user= request.user.id)
    statu = Statu.objects.all()
    return render(request , 'allbooks.html', {'library' : library,'status' : statu})

@login_required
def updateBookState(request , book_id, user_id,state):
    State.objects.filter(book= book_id, user = user_id ).update(statu = state) 
    return redirect('/biblioteca/'+str(state))



#post methd
@login_required
def updateBookProgress(request):
    Progress.objects.filter(
        book = request.POST['book_id'] , 
        user = request.POST['user_id'] , 
    ).update(currentPage =  request.POST['current_page'])
    return HttpResponse('OK')



def login(request):
    if request.user.id is not None:
        return redirect('/biblioteca')

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
           
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                do_login(request, user)
                return redirect('/biblioteca')    
                            
    return render(request, 'home.html')
