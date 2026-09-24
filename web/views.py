from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Flan, ContactForm
from . import forms as f

def indice(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
        'flanes': flanes_publicos
    }
    return render(request, 'web/index.html', context)

def acerca(request):
    return render(request, 'web/about.html')

def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = { 
        'flanes': flanes_privados
    }
    return render(request, 'web/welcome.html', context)

def flan_detail(request, flan_id):
    flan = get_object_or_404(Flan, id=flan_id)
    return render(request, 'web/detail.html', {'flan': flan})

def exito(request):
    return render(request, 'web/exito.html', {})

def contacto(request):
    carrito = request.session.get('carrito', {})

    if carrito:
        tipo_solicitud = 'Pedido Web'
        lineas = ["--- DETALLE DEL PEDIDO ---"]
        total = 0.0
        for item in carrito.values():
            subtotal = item['precio'] * item['cantidad']
            total += subtotal
            lineas.append(f"• {item['cantidad']}x {item['nombre']} - ${subtotal:,.0f}")

        lineas.append(f"\nTOTAL ESTIMADO: ${total:,.0f}")
        lineas.append("--------------------------")
        lineas.append("Dirección de entrega:")
        lineas.append("Fecha:")
        lineas.append("Hora:")
        lineas.append("Notas adicionales:\n")

        mensaje_inicial = "\n".join(lineas)
    else:
        tipo_solicitud = 'Consulta General'
        mensaje_inicial = ""

    if request.method == 'POST':
        form = f.ContactFormModelForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            
            if hasattr(contact, 'tipo_solicitud'):
                contact.tipo_solicitud = tipo_solicitud
            contact.save()

            if 'carrito' in request.session:
                del request.session['carrito']
            return redirect('exito')
        
    else:
        form = f.ContactFormModelForm(initial={'message': mensaje_inicial})

    context = {
        'form': form,
        'tipo_solicitud': tipo_solicitud,
        'tiene_carrito': bool(carrito)
    }
    return render(request, 'web/contacto.html', context)

def agregar_al_carrito(request, flan_id):

    flan = get_object_or_404(Flan, id=flan_id)
    carrito = request.session.get('carrito', {})
    str_id = str(flan_id)
    precio_flan = float(getattr(flan, 'price', getattr(flan, 'precio', 0.0)))

    if str_id in carrito:
        carrito[str_id]['cantidad'] += 1
    else:
        carrito[str_id] = {
            'flan_id': flan.id,
            'nombre': flan.name if hasattr(flan, 'name') else getattr(flan, 'nombre', 'Flan'),
            'precio': precio_flan,
            'cantidad': 1,
        }

    request.session['carrito'] = carrito
    messages.success(request, f'¡Añadido al pedido!')
    return redirect(request.META.get('HTTP_REFERER', 'bienvenido'))


def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    total = 0.0

    items_carrito = []
    for item_id, item in carrito.items():
        subtotal = item['precio'] * item['cantidad']
        total += subtotal
        items_carrito.append({
            'flan_id': item['flan_id'],
            'nombre': item['nombre'],
            'precio': item['precio'],
            'cantidad': item['cantidad'],
            'subtotal': subtotal,
        })

    context = {
        'items_carrito': items_carrito,
        'total_pedido': total,
    }
    return render(request, 'web/ver_carrito.html', context)

def vaciar_carrito(request):
    if 'carrito' in request.session:
        del request.session['carrito']
    messages.info(request, 'Tu carrito de compras ha sido vaciado.')
    return redirect('ver_carrito')
