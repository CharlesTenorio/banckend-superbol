# Generated by Django 3.1.6 on 2021-02-05 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gerentes', '0001_initial'),
        ('cambistas', '0003_cambista_celular'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cambista',
            name='id_banca',
        ),
        migrations.AddField(
            model_name='cambista',
            name='id_gerente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='gerentes.gerente'),
            preserve_default=False,
        ),
    ]
