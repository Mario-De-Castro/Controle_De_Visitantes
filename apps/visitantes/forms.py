from django import forms
from django.forms import fields
from visitantes.models import Visitantes

class VisitantesForm(forms.ModelForm):
    class Meta:
        model = Visitantes
        fields = [
            "nome_completo", "CPF", "data_nascimento", "numero_casa",
            "placa_veiculo"
        ]

class AutorizaVisitanteForm(forms.ModelForm):
    morador_responsavel = forms.CharField(required=True)

    class Meta:
        model = Visitantes
        fields = [
            "morador_responsavel"
        ]
        error_messages = {
            "morador responsavel": {
            "required": "por favor informe o nome do morador resposanvel por autorizar a entrada do visitante"
            }
        }