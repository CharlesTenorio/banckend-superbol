from django.contrib import admin
from .models import Liga

class LigaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cc')
    search_fields = ('nome',)

admin.site.register(Liga, LigaAdmin)

# Register your models here.
