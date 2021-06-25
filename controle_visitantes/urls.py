from django.contrib import admin
from django.urls import path

from usuarios.views import index
from visitantes.views import registrar_visitantes, informacoes_visitante

urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "",
        index,
        name="index"
    ),

    path(
        "registrar-visitantes/",
        registrar_visitantes,
        name="Registro de Visitantes"
    ),

    path(
        "visitantes/<int:id>/",
        informacoes_visitante,
        name="Informacoes Visitantes"
    ),
]
