from django.shortcuts import render

def indice(request):
    return render(request, 'web/index.html')

def acerca(request):
    return render(request, 'web/about.html')

def bienvenido(request):
    return render(request, 'web/welcome.html')