from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from visitantes.models import Visitantes
from visitantes.forms import VisitantesForm

# Create your views here.
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


def informacoes_visitante(request, id):

    visitante = get_object_or_404(Visitantes, id=id)

    context = {
        "nome_pagina": "Informações de visitante",
        "Visitantes": visitante,
    }

    return render(request, "informacoes_visitante.html", context)
