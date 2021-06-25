from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.lookups import StartsWith

# Create your models here.
class Visitantes(models.Model):

    STATUS_VISITANTE = [
        ("AGUARDANDO", "Aguardando autorização"),
        ("EM_VISITA", "Em visita"),
        ("FINALIZADO", "visita Finalizada")
        ]

    status = models.CharField(
        verbose_name="Status",
        max_length=10,
        choices=STATUS_VISITANTE,
        default="AGUARDANDO"
    )

    nome_completo = models.CharField(
        verbose_name="Nome COmpleto",
        max_length=194
    )

    CPF = models.CharField(
        verbose_name="CPF",
        max_length=11
    )

    data_nascimento = models.DateField(
        verbose_name="Data de Nascimento",
        auto_now_add=False,
        auto_now=False
    )

    numero_casa = models.PositiveBigIntegerField(
        verbose_name="Numero da Casa",
    )

    placa_veiculo = models.CharField(
        verbose_name="Placa do veiculo",
        max_length=7,
        blank=True,
        null=True
    )

    horario_chegada = models.DateTimeField(
        verbose_name="Horario de chegada na portarioa",
        auto_now_add=True
    )

    horario_saida = models.DateTimeField(
        verbose_name="Horario de saida do condominio",
        auto_now=False,
        null=True
    )

    horario_autorizacao = models.DateTimeField(
        verbose_name="Horario de autorização de entrada",
        auto_now=False,
        blank=True,
        null=True
    )

    morador_responsavel = models.CharField(
        verbose_name="Morador Responsavel por autorizar a entrada",
        max_length=194,
        blank=True
    )

    registrado_por = models.ForeignKey(
        "porteiros.Porteiro",
        verbose_name="Porteiro responsavel pelo registro",
        on_delete=PROTECT
    )

    def get_horario_saida(self):
        if self.horario_saida:
            return self.horario_saida
        
        return "horario de saida não registrado"

    def get_horario_autorização(self):
        if self.horario_autorizacao:
            return self.horario_autorizacao

        return "Visitante aguardando autorização"

    def get_morador_responsavel(self):
        if self.morador_responsavel:
            return self.morador_responsavel
        
        return "Visitante aguardando autorização"

    def get_placa_veiculo(self):
        if self.placa_veiculo:
            return self.placa_veiculo
        return "veiculo não registrado"

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = "visitante"

    def __str__(self):
        return self.nome_completo