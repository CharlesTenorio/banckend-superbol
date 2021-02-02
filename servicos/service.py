from dataclasses import dataclass
import requests
from decouple import config

@dataclass(init=True, frozen=True)
class LerDadosAPI:
    token:str = 'token='+config("API_TOKEN")
    url_base_v1:str = config("BASE_URL_V1")
    url_base_v2:str = config("BASE_URL_V2")
    time : str = "team"
    sport: str = "1"# tutebol e 1
   
    def lista_times(self):
        url_time = self.url_base_v1+self.time+'?'+self.token+'&sport_id='+self.sport
        r = requests.get(url_time)
        return r

    def lista_ligas(self):
        url_liga = self.url_base_v1+'league?'+self.token+'&sport_id='+self.sport
        r= requests.get(url_liga)
        return r

    def lista_ligas_tabela(self, id_liga):
        # https://api.b365api.com/v2/league/table?token=74409-ok98vsO3htGHPn&league_id=155
        url_liga_tlb = self.url_base_v2+'league/table?'+self.token+'&league_id='+str(id_liga)
        r= requests.get(url_liga_tlb)
        return r    
