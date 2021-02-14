from celery import shared_task
from .services import incluir_times




@shared_task
def import_times():
   OK= incluir_times()
   return OK
    