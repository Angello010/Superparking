from django.contrib import admin
from django.urls import include, path 
from apps.tiempo.views import *
from apps.permisos.views import *
from apps.medios_de_pago.views import *
from apps.tiempodeparqueo.views import *
from apps.usuarios.views import *
from apps.vehiculo.views import *
from apps.tipo_de_factura.views import *
from apps.rol.views import *
from apps.horadeparqueo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.routers')),
   
    path('tiempo/', TiempoViewset.as_view(template_name='template/tiempo.html')),
    path('permisos/', PermisosViewset.as_view(template_name='template/tiempo.html')),
    path('medios_de_pago/', Medios_de_pagoViewset.as_view(template_name='template/tiempo.html')),
    path('rol/', RolViewset.as_view(template_name='template/tiempo.html')),
    path('tiempo_de_parqueo/', TiempodeparqueoViewset.as_view(template_name='template/tiempo.html')),
    path('usuarios/', UsuariosViewset.as_view(template_name='template/tiempo.html')),
    path('vehiculo/', VehiculoViewset.as_view(template_name='template/tiempo.html')),
    path('tipo_de_factura/', Tipo_de_facturaViewset.as_view(template_name='template/tiempo.html')),
    path('horadeparqueo/', HoradeparqueoViewset.as_view(template_name='template/tiempo.html')),


]