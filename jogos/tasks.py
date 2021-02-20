from celery import shared_task
from servicos.service import LerDadosAPI
from datetime import datetime
from ligas.models import Liga
from .models import Jogo
from dataclasses import dataclass


def timestamp_pra_datetime(data_timestamp):
    dt_object = datetime.fromtimestamp(data_timestamp)
    data_text= dt_object.strftime("%d/%m/%Y %H:%M:%S")
    data_e_hora = datetime.strptime(data_text, '%d/%m/%Y %H:%M:%S')
    
    #data_txt = dt_object.strftime('%d/%m/%Y %H:%M:%s')
    #data_correta = datetime.strptime(data_txt, '%d/%m/%Y %H:%M')
    return data_e_hora

    


@dataclass
class MontarJogos:
    id_partida: int
    id_time_casa: int
    time_casa:str
    id_time_visitante: int
    time_visitante: str
    id_liga: int
    liga: str
    cc: str
    ss: str
    data_partida: int
    qtd_gol_casa: int
    qtd_gol_visitante: int
    realizada : bool

    
@shared_task
def incluir_jogos_novos():
    jogos = LerDadosAPI()
    lista_liga = Liga.objects.all()
    salva = False
    data_jogo=None 
     
    try:
        
          for liga in lista_liga:
             result = jogos.listar_jogos('Novos', 155)
             
             if result:
                
               
                     for i  in result['results']:
             
                        p = MontarJogos(i["id"],
                                       i["home"]["id"],
                                       i["home"]["name"],
                                       i["away"]["id"],
                                       i["away"]["name"],
                                       i["league"]["id"],
                                       i["league"]["name"],
                                       i["league"]["cc"],  
                                       i["ss"],
                                       i["time"],
                                       0,
                                       0,
                                       False)

                        data_jogo=timestamp_pra_datetime(p.data_partida)             
                        
                        jg =     Jogo(id_partida=p.id_partida,
                                      id_time_casa=p.id_time_casa,
                                      time_casa=p.time_casa,
                                      id_time_visitante=p.id_time_visitante,
                                      time_visitante=p.time_visitante,
                                      id_liga=p.id_liga,
                                      liga=p.liga,
                                      cc=p.cc,
                                      ss=p.ss,
                                      data_partida=data_jogo,
                                      qtd_gol_casa=p.qtd_gol_casa,
                                      qtd_gol_visitante=p.qtd_gol_visitante,
                                      realizada=p.realizada)
                        jg.save()           

                        
                     print(partida)        
    except Exception as e:
        print(str(e))
        
                     
                    

    return salva                         
