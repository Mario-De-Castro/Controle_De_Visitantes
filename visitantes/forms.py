from django import forms
from visitantes.models import Visitantes

class VisitantesForm(forms.ModelForm):
    class Meta:
        model = Visitantes
        fields = [
            "nome_completo", "CPF", "data_nascimento", "numero_casa",
            "placa_veiculo"
        ]