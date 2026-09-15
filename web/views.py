from django.shortcuts import render
from .models import Flan

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


