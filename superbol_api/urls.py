from django.contrib import admin
from django.urls import path
from times.views import get_times
urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_times/', get_times, name='get_times')
]


admin.site.site_header = "Super Boll"

admin.site.index_title = "Super Boll"

admin.site.site_title = "Super Boll"
