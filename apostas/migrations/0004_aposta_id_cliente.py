# Generated by Django 3.1.5 on 2021-01-31 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20210131_1942'),
        ('apostas', '0003_aposta_id_cambista'),
    ]

    operations = [
        migrations.AddField(
            model_name='aposta',
            name='id_cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.cliente'),
        ),
    ]
