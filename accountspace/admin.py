from django.contrib import admin
from .models import User, Bewerber
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.
admin.site.register(User, BaseUserAdmin)
admin.site.register(Bewerber)