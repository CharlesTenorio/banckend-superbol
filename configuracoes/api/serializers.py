from rest_framework import serializers, request
from rest_framework.serializers import ModelSerializer
from configuracoes.models import Configuracao



class ConfiguracaoSerializer(ModelSerializer):

    class Meta:
        model = Configuracao
        fields = ['id_banca', 'val_min_aposta', 'val_max_aposta', 'val_max_aposta_aovivo', 'premio_maximo', 
                   'contacao_mini_bilhete', 'cotacaomaxima_Bilhete', 'nao_exibir_cotacoes_menores',
                   'qtd_mini_jogos_bilhetes', 'qtd_max_jogos_bilhetes', 'texto_rodape', 'email_alerta', 'cambista_cancelar_bilhete',
                   'exibir_bilhetes_gerentes_camistas', 'tempo_cancelamento', 'apostas_ativas', 'alertar_apostas_acima', 
                   'alertar_apostas_simples_contacao_acima', 'alertar_apostas_multiplas_contacao_acima', 
                   'limite_aposta_simples_todos_cambistas', 'limite_aposta_geral_todos_cambistas', 'val_max_contacoes', 
                    'comissao_padrao', 'nome_url']

      