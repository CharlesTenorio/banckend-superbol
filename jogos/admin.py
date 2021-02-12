from django.contrib import admin
from .models import Jogo

class JogoAdmin(admin.ModelAdmin):
    list_display = ('id_partida', 'time_casa','time_visitante', 'data_partida')
    search_fields = ('time_casa', 'time_visitante' )

admin.site.register(Jogo, JogoAdmin)
# Register your models here.
