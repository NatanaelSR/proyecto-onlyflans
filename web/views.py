from django.shortcuts import render, redirect
from .models import Flan, ContactForm
from . import forms as f

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
