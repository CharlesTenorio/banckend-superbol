from celery import shared_task
from .service import incluir_jogos_novos, incluir_ligas
import pandas as pd
from jogos.models import jogo


def timestamp_pra_datetime(data_timestamp):
    dt_object = datetime.fromtimestamp(timestamp)
    data_txt = dt_object.strftime('%d/%m/%Y %H:%M:%s')
    data_correta = datetime.strptime(data_txt, ‘%d/%m/%Y %H:%M’)
    return data_correta

@shared_task
def import_jogos():
   
    df = incluir_jogos_novos()

    if not df.empty:
        for i in df.itertuples():
            jg = jogo(id_partida=i.id_partida,
                      id_time_casa=i.id_time_casa,
                      time_casa=i.time_casa,
                      id_time_visitante=i.id_time_visitante,
                      time_visitante= i.time_visitante,
                      id_liga=i.id_liga
                      liga=i.liga,
                      cc=i.cc,
                      ss=i.ss,
                      data_partida = timestamp_pra_datetime(i.data_timestamp),
                      qtd_gol_casa=0,
                      qtd_gol_visitante=0,
                      realizada=False
                      )
