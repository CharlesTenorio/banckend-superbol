from django.db import models

class Time(models.Model):
    id_time = models.IntegerField(primary_key=True)
    nome_time = models.CharField(max_length=80, null=False, blank=False, unique=True)
    cc = models.CharField(max_length=2, blank=True, null=True)
    image_id = models.IntegerField(null=False, blank=False, default=0)
    data_cad= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome_time

    class Meta:
        db_table = 'time'
        managed = True
        verbose_name = 'Time'
        verbose_name_plural = 'Times'


class Risco(models.Model):
    id_time = models.ForeignKey(Time, on_delete=models.PROTECT)
    descricao_risco= models.CharField(max_length=40)
    valor_risco = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.descricao_risco

    class Meta:
        db_table = 'risco'
        managed = True
        verbose_name = 'Risco'
        verbose_name_plural = 'Riscos'
