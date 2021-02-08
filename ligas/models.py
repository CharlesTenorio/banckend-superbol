from django.db import models

class Liga(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    nome= models.CharField(max_length=80)
    cc=models.CharField(max_length=2, blank=True, null=True)
    has_leaguetable=models.IntegerField()
    has_toplist=models.IntegerField()

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'liga'
        managed = True
        verbose_name = 'Liga'
        verbose_name_plural = 'Ligas'



# Create your models here.
