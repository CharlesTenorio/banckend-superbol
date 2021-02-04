from django.contrib import admin
from .models import Configuracao

class ConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_banca')
   

admin.site.register(Configuracao, ConfigAdmin)



# Register your models here.
