from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Clientes, Articulos, Pedidos
from django.core.mail import send_mail
from django.conf import settings

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


# Vista para el formulario de contacto:
def contacto(request):

    if request.method == 'POST':

        subject = request.POST["subject"]
        message = request.POST["message"] + " " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["noxgnox0@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)

        return render(request, "gracias.html")

    return render(request, "contacto.html")
