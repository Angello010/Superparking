from django.contrib import admin
from django.urls import include, path 
from apps.usuarios import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.routers')),
    path('login/', auth_views.LoginView.as_view(template_name='horadeparqueo/login.html'),
name='login'),
    path('registrate/', auth_views.LoginView.as_view(template_name='medios_de_pago/registrate.html'),
name='registrate'),
    path('pagina_inicio/', auth_views.LoginView.as_view(template_name='permisos/pagina_inicio.html'),
name='pagina_inicio'),
    path('rol/', auth_views.LoginView.as_view(template_name='rol/tiempo.html'),
name='rol'),


]
