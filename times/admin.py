from django.contrib import admin
from .models import Time, Risco

class TimeAdmin(admin.ModelAdmin):
    list_display = ('id_time', 'nome_time', 'cc')
    search_fields = ('nome_time', )

admin.site.register(Time, TimeAdmin)
admin.site.register(Risco)



# Register your models here.
