# Generated by Django 3.2.4 on 2021-06-22 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitantes',
            name='status',
            field=models.CharField(choices=[('AGUARDANDO', 'Aguardando autorização'), ('EM_VISITA', 'Em visita'), ('FINALIZADO', 'visita Finalizada')], default='AGUARDANDO', max_length=10, verbose_name='Status'),
        ),
    ]
