from django.contrib import admin
from .models import Cliente, Conta, HistorioConta

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome','cpf')
    search_fields = ('nome', )

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Conta)
admin.site.register(HistorioConta)



# Register your models here.
