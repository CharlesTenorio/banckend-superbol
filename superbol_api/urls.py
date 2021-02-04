from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]


admin.site.site_header = "Super Boll"

admin.site.index_title = "Super Boll"

admin.site.site_title = "Super Boll"
