# Generated by Django 3.1.6 on 2021-02-08 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='liga',
            name='has_leaguetable',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]