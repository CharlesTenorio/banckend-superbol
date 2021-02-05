from django.contrib import admin
from .models import Administrador

class AdmAdministrador(admin.ModelAdmin):
    list_display = ('id_usuario', 'id_banca','nome', 'celular')
    search_fields = ('nome', )

admin.site.register(Administrador, AdmAdministrador)


# Register your models here.
