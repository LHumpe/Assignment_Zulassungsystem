from django.contrib import admin
from .models import User, Bewerber
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{
            'fields':('first_name','last_name','email', 'is_ausschuss', ),
        }),
    )
# Register your models here.
admin.site.register(User, CustomUserAdmin)
admin.site.register(Bewerber)
