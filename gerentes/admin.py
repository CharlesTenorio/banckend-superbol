from django.contrib import admin
from .models import Gerente


class GerenteAdm(admin.ModelAdmin):
    list_display = ('id_usuario', 'id_adm','nome', 'celular')
    search_fields = ('nome', )

admin.site.register(Gerente, GerenteAdm)


# Register your models here.
