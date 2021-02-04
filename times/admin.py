from django.contrib import admin
from .models import Time, Risco

class OticaAdmin(admin.ModelAdmin):
    list_display = ('id_time', 'nome_time', 'cc')
    search_fields = ('nome_time')



# Register your models here.
