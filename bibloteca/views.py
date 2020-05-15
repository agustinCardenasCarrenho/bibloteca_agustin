from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate ,login as do_login
from django.contrib.auth.forms import AuthenticationForm
from .models import Statu , Library ,Book , Progress


def home(request):
    return render(request ,'home.html' )

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
    return redirect('/bibloteca/'+str(state))



#post methd
def updateBookProgress(request):
    Progress.objects.filter(
        book = request.POST['book_id'] , 
        user = request.POST['user_id'] , 
    ).update(currentPage =  request.POST['current_page'])
    return HttpResponse('OK')

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')
    return render(request, "user/login.html", {'form': form})

