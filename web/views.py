from django.shortcuts import render, redirect,get_object_or_404
from .models import Flan, ContactForm
from . import forms as f
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required

def indice(request):
    return render(request, 'web/index.html')

def acerca(request):
    return render(request, 'web/about.html')

def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = { 
        'flanes': flanes_privados
    }
    return render(request, 'web/welcome.html', context)

def indice(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
        'flanes': flanes_publicos
    }

    return render(request, 'web/index.html', context)


def contacto(request):
    if request.method == 'POST':
        form = f.ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return redirect('exito')
    else:
        form = f.ContactFormForm()
    return render(request, 'web/contacto.html',{'form' : form})

def exito(request):
        return render(request, 'web/exito.html',{})


def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('indice')

    else:
        form = AuthenticationForm()

    return render(request, 'web/login.html', { 'form': form })

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('indice')

    else:
        form = UserCreationForm()

    return render(request, 'web/signup.html', { 'form': form })

def log_out(request):
    logout(request)
    return redirect('indice')