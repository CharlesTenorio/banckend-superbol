from servicos.service import LerDadosAPI
from datetime import datetime
from ligas.models import Liga
from .models import jogo
import pandas as pd


#TODO TERMINAR AMANHA COM PANSDA
def incluir_ligas():
    salvar = False
    try:
        
      qtd_ligas = Liga.objects.count()
      if qtd_ligas <= 0:
        obj_ligas = LerDadosAPI()
        ligas = obj_ligas.listar_ligas()
        if ligas:
            for liga in ligas["results"]:
                lg = Liga(id=liga['id'],
                     nome=liga['name'],
                     cc=liga['cc'],
                     has_leaguetable=liga["has_leaguetable"],
                     has_toplist=liga["has_toplist"])
                     

                lg.save() 
                salvar=True         
    except Exception as e:
        print(str(e))
        salvar=False
    return salvar    

    
def incluir_jogos_novos():
    jogos = LerDadosAPI()
    lista_liga = Liga.objects.all()
    df = pd.DataFrame(columns=['id_partida', 'id_time_casa', 'time_casa', 'id_time_visitante', 'time_visitante', 'id_liga',
                              'liga', 'cc', 'ss', 'data_partida', 'qtd_gol_casa', 'qtd_gol_visitante', 'realizada'] )  
    
    for liga in lista_liga:
         result = jogos.listar_jogos('Novos', str(liga.id))
         if result:

             for i  in result['results']:
                 df = df.append({"id_partida": i["id"],
                                 "id_time_casa": i["home"]["id"],
                                 "time_casa": i["home"]["name"],
                                 "id_time_visitante": i["away"]["id"],
                                 "time_visitante": i["away"]["name"],
                                 "id_liga": i["league"]["id"],
                                 "liga": i["league"]["name"],
                                 "cc": i["cc"],
                                 "ss": i["ss"],
                                 "data_partida": i["time"],
                                 "cc": i["cc"],
                                 "qtd_gol_casa": 0,
                                 "qtd_gol_visitante": 0,
                                 "realizada": False })  

    return df                         
             