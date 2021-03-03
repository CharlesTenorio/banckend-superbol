from django.contrib import admin
from .models import PlanoContas, ContasPagar, ContasReceber

class PlanoAdmin(admin.ModelAdmin):
    list_display = ('id', 'plano_conta')
    search_fields = ('plano_conta', )


class CotasPgAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'id_banca','descricao', 'valor_total', 'status_pg')
    search_fields = ('descricao', )


class ContasRecebAdmin(admin.ModelAdmin):
    list_display = ('id_plano', 'id_banca','descricao', 'valor_tota')
    search_fields = ('descricao', 'status_rebe')

admin.site.register(PlanoContas, PlanoAdmin)

admin.site.register(ContasPagar, CotasPgAdmin)

admin.site.register(ContasReceber, ContasRecebAdmin)












# Register your models here.
