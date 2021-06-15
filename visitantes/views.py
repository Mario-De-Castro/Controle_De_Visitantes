from django.shortcuts import render
from visitantes.forms import VisitantesForm

# Create your views here.
def registrar_visitantes(request):

    form = VisitantesForm()

    if request.method == "POST":
        form = VisitantesForm(request.POST)

        if form.is_valid():
            form.save()

    context = {
        "nome_pagina": "Registrar Visitantes",
        "form": form
    }

    return render(request, "registrar_visitante.html", context)