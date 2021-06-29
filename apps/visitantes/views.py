from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from visitantes.models import Visitantes
from visitantes.forms import VisitantesForm, AutorizaVisitanteForm
from django.utils import timezone
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required

@login_required
def registrar_visitantes(request):

    form = VisitantesForm()

    if request.method == "POST":
        form = VisitantesForm(request.POST)

        if form.is_valid():
            visitante = form.save(commit=False)

            visitante.registrado_por = request.user.porteiro
            visitante.save()

            messages.success(request, "Visitante cadastrado com Sucesso")

            return redirect("index")

    context = {
        "nome_pagina": "Registrar Visitantes",
        "form": form
    }

    return render(request, "registrar_visitante.html", context)

@login_required
def informacoes_visitante(request, id):

    visitante = get_object_or_404(Visitantes, id=id)

    form = AutorizaVisitanteForm()

    if request.method == "POST":
        form = AutorizaVisitanteForm(
            request.POST,
            instance=visitante
            )
        if form.is_valid():
            form.save(commit=False)

            visitante.status = "EM VISITA"
            visitante.horario_autorizacao = timezone.now()

            visitante.save()

            messages.success(
                request,
                "Entrada de visitante autorizada com sucesso"
            )

            return redirect("index")

    context = {
        "nome_pagina": "Informações de visitante",
        "visitante": visitante,
        "form": form,
    }

    return render(request, "informacoes_visitante.html", context)

@login_required
def finalizar_visita(request, id):

    if request.method == "POST":
        visitante = get_object_or_404(
            Visitantes,
            id=id
        )
        visitante.status = "FINALIZADO"
        visitante.horario_saida = timezone.now()

        visitante.save()

        messages.success(
            request,
            "Visita Finalizada com sucesso"
        )

        return redirect("index")

    else:
        return HttpResponseNotAllowed(
            ["POST"],
            "Metódo Não permitido"
        )