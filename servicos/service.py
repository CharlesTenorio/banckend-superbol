from dataclasses import dataclass
import requests
from decouple import config
from datetime import datetime
import json
from typing import Dict

token = config("API_TOKEN")


urls={
        "times": "https://api.b365api.com/v1/team?token="+token+"&sport_id=1&page=",
        "ligas": "https://api.b365api.com/v1/league?token="+token+"&sport_id=1&page=",
        "upcoming_events" : "https://api.b365api.com/v2/events/upcoming?sport_id=1&token="+token, 
        "event_view":"https://api.b365api.com/v1/event/view?token="+token+"&event_id=",
        "ended_events" : "https://api.b365api.com/v2/events/ended?sport_id=1&token="+token,
        "envents_odds_summarys" :"https://api.b365api.com/v2/event/odds/summary?token="+token+"&event_id=",
        "events_search": "https://api.b365api.com/v1/events/search?token="+token+"&sport_id=1&home=",
        "odds":"https://api.b365api.com/v2/event/odds?token="+token+"&event_id="

     }
   

@dataclass(frozen=True)
class LerDadosAPI:
    
    def qtd_paginas_registros(self, url):
        r = requests.get(url).json()
        total = 0
        total_registro=int(r['pager']["total"])
        num_pagina=0
        num_pg = int(r['pager']['per_page'])
        num_pagina = total_registro/num_pg
        return num_pagina
    
    
    def listar_times(self, pagina):
       
        url_time = urls["times"]+str(pagina)
        r = requests.get(url_time)
        #timesbr = [ x for x in times['results'] if x['cc'] == 'br' ]
        return r.json()

    
    def listar_ligas(self, pagina):
        url_liga = urls["ligas"]+str(pagina)
        r= requests.get(url_liga)
        return r.json()

    
    def listar_ligas_tabela(self, id_liga):
       
        url_liga_tlb = self.url_base_v2+'league/table?'+self.token+'&league_id='+str(id_liga)
        r= requests.get(url_liga_tlb)
        return r.json()    
    
    def listar_jogos(self, tipo_jogo, league_id, pagina):
        url_jogos = ''
        if tipo_jogo == 'Novos':
            url_jogos = 'https://api.b365api.com/v2/events/upcoming?sport_id=1&league_id='+str(league_id)+'&token='+token+'&page='+str(pagina)
           
        else:
            url_jogos='https://api.b365api.com/v2/events/ended?sport_id=1&league_id='+str(league_id)+'&token='+token+'&page='+str(pagina)

        r= requests.get(url_jogos)
        return r.json()      
     
    def procurar_jogo(self, time_casa, time_visitante, data_jogo):
        ''' data do jogo e convertido pra timestamp'''
        timestamp = datetime.timestamp(data_jogo)
        dt = int(timestamp)
        url_jogo = urls["events_search"]+time_casa+"&away="+time_visitante+"&time="+str(dt)
        print(url_jogo)
        r = requests.get(url_jogo)
        return r.json()

    def listar_eventos(self, id_liga):
        url_liga_tlb = self.url_base_v2+'league/table?'+self.token+'&league_id='+str(id_liga)
        r= requests.get(url_liga_tlb)
        return r.json()    
   

