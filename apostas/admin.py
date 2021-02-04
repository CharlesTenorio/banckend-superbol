from django.contrib import admin
from .models import Aposta

class ApostaAdmin(admin.ModelAdmin):
    list_display = ('id_aposta', 'id_banca', 'id_cambista','id_cliente', 'tipo')
    search_fields = ('id_aposta', )

admin.site.register(Aposta, ApostaAdmin)


# Register your models here.
