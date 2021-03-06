from celery import shared_task
from servicos.service import LerDadosAPI, urls
from .models import Time


@shared_task
def incluir_times():
    salvar = False
    img_code = 0
    code_img =0
    try:
        
      qtd_time = Time.objects.count()
      if qtd_time <= 0:
        obj_times = LerDadosAPI()
        t = urls["times"]+"1"
        qtd_pg = int(obj_times.qtd_paginas_registros(t))
        for i in range(506):
            times = obj_times.listar_times(i)
            if times:
              for t in times["results"]:

                  if t['image_id']== None:
                      code_img=0
                  else:
                      code_img= t["image_id"]    

                  time = Time(id_time=t["id"],
                            nome_time=t["name"],
                            cc=t["cc"], 
                            image_id=code_img)

                  time.save() 
            
        salvar=True         
    except Exception as e:
        print(str(e))
        salvar=False
    return salvar    
