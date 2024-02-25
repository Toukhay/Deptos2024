from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import USUARIO


def home(request):
    return render(request, 'applist/home.html')

def about(request):
    return render(request, 'applist/about.html')

def contact(request):
    return render(request, 'applist/contact.html')

def listings(request):
    return render(request, 'applist/listings.html')

def login(request):
    return render(request, 'applist/login.html')

def register(request): # Vista para el registro de usuarios
    if request.method == 'POST': # Si el usuario envía el formulario de registro
        form = UserCreationForm(request.POST) # Se crea un formulario de registro con los datos del usuario
        if form.is_valid(): # Si el formulario es válido, se guarda el usuario en la base de datos
            form.save() # Se guarda el usuario en la base de datos
            username = form.cleaned_data.get('username') # Se obtiene el nombre de usuario del formulario
            raw_password = form.cleaned_data.get('password1') # Se obtiene la contraseña del formulario
            user = authenticate(username=username, password=raw_password) # Se autentica al usuario
            login(request, user) # Se inicia sesión con el usuario
            return redirect('home') # Redirige al usuario a la página de inicio después de registrarse
    else:
        form= UserCreationForm() # Si el usuario no ha enviado el formulario, se muestra el formulario de registro
    return render(request, 'applist/register.html', {'form': form}) # Si el formulario no es válido, se muestra de nuevo el formulario de registro con los errores

def search(request):
    return render(request, 'applist/search.html')

def view_property(request):
    return render(request, 'applist/view_property.html')
