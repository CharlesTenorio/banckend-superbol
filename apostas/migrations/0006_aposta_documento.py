# Generated by Django 3.1.5 on 2021-01-31 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apostas', '0005_aposta_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='aposta',
            name='documento',
            field=models.CharField(default='cpf', max_length=20),
        ),
    ]
