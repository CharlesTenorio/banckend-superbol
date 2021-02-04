from django.db import models
from bancas.models import Banca

class Configuracao(models.Model):
    id_banca = models.ForeignKey(Banca, on_delete=models.PROTECT, blank=False, null=False)
    val_min_aposta= models.DecimalField(max_digits=9, decimal_places=2)
    val_max_aposta= models.DecimalField(max_digits=9, decimal_places=2)
    val_max_aposta_aovivo = models.DecimalField(max_digits=9, decimal_places=2)
    premio_maximo = models.DecimalField(max_digits=9, decimal_places=2)
    contacao_mini_bilhete=models.DecimalField(max_digits=9, decimal_places=2)
    npg_comissão_apostas_cota_menor = models.DecimalField(verbose_name='Não pagar comissão em apostas com cota menor que:',
                                                          max_digits=9, decimal_places=2, default=1)
    cotacaomaxima_Bilhete = models.DecimalField(verbose_name='Cotação Máxima no Bilhete',
                                                          max_digits=9, decimal_places=2, default=1)
    nao_exibir_cotacoes_menores = models.DecimalField(verbose_name='Não Exibir Cotações Menores Que:',
                                                          max_digits=9, decimal_places=2, default=1) 
    qtd_mini_jogos_bilhetes = models.PositiveIntegerField(verbose_name='Quantidade mínima de jogos por bilhete:', default=1)
    qtd_max_jogos_bilhetes = models.PositiveIntegerField(verbose_name='Quantidade máxima de jogos por bilhete:', default=1)
    texto_rodape= models.CharField(max_length=80, default='Valor maximo pago no premio é de R$50.000,00')
    email_alerta = models.EmailField(max_length=150)
    cambista_cancelar_bilhete = models.BooleanField(default=True)
    exibir_bilhetes_gerentes_camistas = models.BooleanField(default=True)
    tempo_cancelamento = models.PositiveIntegerField(default=15)
    apostas_ativas = models.BooleanField(default=True)
    alertar_apostas_acima = models.DecimalField(verbose_name='Alertar apostas acima de:', 
                                                          max_digits=9, decimal_places=2, default=1)
    alertar_apostas_simples_contacao_acima = models.DecimalField(verbose_name='Alertar cupons de apostas simples com cotações acima de:', 
                                                          max_digits=9, decimal_places=2) 
    alertar_apostas_multiplas_contacao_acima = models.DecimalField(verbose_name='Alertar cupons de apostas múltiplas com cotação acima de:', 
                                                          max_digits=9, decimal_places=2) 
    limite_aposta_simples_todos_cambistas = models.PositiveIntegerField(verbose_name='Limite de apostas simples de todos os cambistas após prestar contas:')
    limite_aposta_geral_todos_cambistas = models.PositiveIntegerField(verbose_name='Limite de apostas geral de todos os cambistas após prestar contas:')
    val_max_contacoes = models.DecimalField(verbose_name='Valor Máximo para Cotações', max_digits=9, decimal_places=2)
    comissao_padrao = models.DecimalField(verbose_name='Comissão padrão (%):', max_digits=9, decimal_places=2)
    comissao_padrao_ao_vivo = models.DecimalField(verbose_name='Comissão padrão ao vivo (%):', max_digits=9, decimal_places=2)
    logo_banca = models.ImageField(null=True, )

    def __str__(self):
            return self.id_banca

    class Meta:
        db_table = 'configuracao'
        managed = True
        verbose_name = 'Configuracao'
        verbose_name_plural = 'Configurações'


# Create your models here.
