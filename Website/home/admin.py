from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class Useradmin(admin.ModelAdmin):
    list_display=("username","first_name","email","mob")
    fields=("username","first_name","email","mob","password",)

admin.site.register(User, Useradmin)
