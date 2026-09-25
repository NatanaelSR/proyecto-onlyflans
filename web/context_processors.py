

def carrito_counter(request):

    carrito = request.session.get('carrito', {})
    total_unidades = 0

    if isinstance(carrito, dict):
        for item in carrito.values():
            if isinstance(item, dict):
                total_unidades += item.get('cantidad', 0)
            elif isinstance(item, int):
                total_unidades += item

    return {
        'total_unidades_carrito': total_unidades
    }