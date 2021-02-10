from celery import shared_task
from .servicos import incluir_jogos_novos, incluir_ligas
import pandas as pd
from .models import jogo




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
                      id_liga=i.id_liga,
                      liga=i.liga,
                      cc=i.cc,
                      ss=i.ss,
                      data_partida = i.data_timestamp,
                      qtd_gol_casa=0,
                      qtd_gol_visitante=0,
                      realizada=False
                      )
