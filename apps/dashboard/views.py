from django.contrib.auth import login
from django.shortcuts import render
from visitantes.models import Visitantes
from django.contrib.auth.decorators import login_required

from django.utils import timezone

@login_required
def index(request):

    todos_visitantes = Visitantes.objects.order_by(
        "-horario_chegada"
    )

    visitantes_aguardando = todos_visitantes.filter(
        status="AGUARDANDO"
    )

    visitantes_em_visita = todos_visitantes.filter(
        status="EM_VISITA"
    )

    visitantes_finalizado = todos_visitantes.filter(
        status="FINALIZADO"
    )

    hora_atual = timezone.now()
    mes_atual = hora_atual.month
    
    #Lookups
    visitantes_mes = todos_visitantes.filter(
        horario_chegada__month=mes_atual
    )

    #Necessario declarar aqui para visualizar no template.
    context = {
        "nome_pagina": "Inicio da Dashboard",
        "todos_visitantes": todos_visitantes,
        "visitantes_aguardando": visitantes_aguardando.count(),
        "visitantes_em_visita": visitantes_em_visita.count(),
        "visitantes_finalizado": visitantes_finalizado.count(),
        "visitantes_mes": visitantes_mes.count(),
    }


    return render(request, "index.html", context)