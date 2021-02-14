from servicos.service import LerDadosAPI
from .models import Liga


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

