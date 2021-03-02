from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from usuarios.models import User



admin.site.register(User)
list_display = ('id',  'email')

