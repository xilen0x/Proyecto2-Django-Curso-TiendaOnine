from django.contrib import admin

from gestionPedidos.models import Clientes, Articulos, Pedidos

# list_display para ver otros campos en el panel admin, como por ej.además del nombre del cliente, creamos la siguiente clase q hereda de admin.ModelAdmin:
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","email","telefono")
    #search_fields para agregar un campo de búsqueda y q permita buscar por 'nombre' y 'telefono' :
    search_fields=("nombre","telefono")

#list_filter para agregar un filtro y q filtre por 'seccion':
class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",)

#para agregar un filtro de fecha:
class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha" #esta linea es para ver el menú filtro tipo link q aparece arriba horizontalmente.

#Para tener disponible desde el panel administración las tablas creadas en e archivo models.py:
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
