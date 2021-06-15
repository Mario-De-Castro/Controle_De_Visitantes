from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.
class Visitantes(models.Model):

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

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = "visitante"

    def __str__(self):
        return self.nome_completo