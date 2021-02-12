from servicos.service import LerDadosAPI
from datetime import datetime
from ligas.models import Liga
from .models import Jogo



def timestamp_pra_datetime(data_timestamp):
    dt_object = datetime.fromtimestamp(data_timestamp)
    data_text= dt_object.strftime("%d/%m/%Y %H:%M:%S")
    data_e_hora = datetime.strptime(data_text, '%d/%m/%Y %H:%M:%S')
    
    #data_txt = dt_object.strftime('%d/%m/%Y %H:%M:%s')
    #data_correta = datetime.strptime(data_txt, '%d/%m/%Y %H:%M')
    return data_e_hora

    

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
    salva = False
   
   
    try:
        
          for liga in lista_liga:
             result = jogos.listar_jogos('Novos', liga.id)
             if result:
               
                     for i  in result['results']:
                        
                        jg = Jogo(id_partida = i["id"],
                                id_time_casa = i["home"]["id"],
                                time_casa = i["home"]["name"],
                                id_time_visitante = i["away"]["id"],
                                time_visitante = i["away"]["name"],
                                id_liga = i["league"]["id"],
                                liga = i["league"]["name"],
                                cc = i["league"]["cc"],
                                ss = i["ss"],
                                data_partida = i["time"],
                                qtd_gol_casa = 0,
                                qtd_gol_visitante = 0,
                                realizada = False)
                        jg.salve()
                        salve = True
    except Exception as e:
        print(srt(e))
        
                     
                    

    return salva                         

