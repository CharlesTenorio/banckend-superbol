from celery import shared_task
from .servicei import incluir_ligas

@shared_task
def import_ligas():
   OK= incluir_ligas()
   return OK
    