from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Clientes, Articulos, Pedidos

# Create your views here.


def busqueda_productos(request):

    return render(request, "busqueda_productos.html")


def buscar(request):
    # Validacion de la búsqueda:
    if request.GET["prod"]:
        # obtenemos lo que el usuario ingresó en el input prod y enviams un mensaje:
        #mensaje="Artículo buscado: %r" %request.GET["prod"]
        producto = request.GET["prod"]
        if len(producto) > 30:
            mensaje = "Texto demasiado largo!"
        else:
            # Este es como un select de la tabla Articulos donde x=producto
            articulos = Articulos.objects.filter(nombre__icontains=producto)
            return render(request, "resultados_busqueda.html", {"articulos": articulos, "query": producto})

    else:
        mensaje = "Debes introducir algún producto para buscar!"

    return HttpResponse(mensaje)

def contacto(request):

    return render(request, "contacto.html")
    