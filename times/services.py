from servicos.service import LerDadosAPI
from .models import Time


def incluir_times():
    salvar = False
    img_code = 0
    code_img =0
    try:
        
      qtd_time = Time.objects.count()
      if qtd_time <= 0:
        obj_times = LerDadosAPI()
        times = obj_times.listar_times()
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



