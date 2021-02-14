from celery import shared_task
from .servicos import incluir_jogos_novos

@shared_task
def import_jogos():
    incluir_jogos_novos()

    