from django.contrib import admin
from django.urls import path
from times.views import get_times
from ligas.views import get_ligas


urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_times/', get_times, name='get_times'),
    path('get_ligas/', get_ligas, name='get_ligas'),
]



admin.site.site_header = "Super Boll"

admin.site.index_title = "Super Boll"

admin.site.site_title = "Super Boll"
