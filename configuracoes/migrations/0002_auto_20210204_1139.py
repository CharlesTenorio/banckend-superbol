# Generated by Django 3.1.6 on 2021-02-04 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracao',
            name='logo_banca',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='configuracao',
            name='nome_url',
            field=models.CharField(default='banca', max_length=20),
        ),
    ]
