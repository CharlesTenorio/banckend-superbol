# Generated by Django 3.1.5 on 2021-01-31 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apostas', '0004_aposta_id_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='aposta',
            name='nome',
            field=models.CharField(default='jose', max_length=40),
            preserve_default=False,
        ),
    ]
