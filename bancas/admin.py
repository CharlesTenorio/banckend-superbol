from django.contrib import admin
from .models import Banca

class BancaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_banca', 'resposavel_banca', 'celular')
    search_fields = ('nome_banca', )

admin.site.register(Banca, BancaAdmin)


# Register your models here.
