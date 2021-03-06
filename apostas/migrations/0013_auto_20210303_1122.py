# Generated by Django 3.1.7 on 2021-03-03 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apostas', '0012_detalheaposta'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalheaposta',
            name='cotacao',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AddField(
            model_name='detalheaposta',
            name='liga',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detalheaposta',
            name='status',
            field=models.CharField(default='Aberta', max_length=40),
        ),
        migrations.AddField(
            model_name='detalheaposta',
            name='status_cotacao',
            field=models.CharField(choices=[('Casa', 'Casa'), ('Fora', 'Fora'), ('Empate', 'Empate')], default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detalheaposta',
            name='time_casa',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detalheaposta',
            name='time_visitante',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]
