from django.contrib import admin
from .models import User, Bewerber
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'is_ausschuss',),
        }),
    )

    def get_queryset(self, request):
        qs = super(CustomUserAdmin, self).get_queryset(request)
        if request.user.is_ausschuss == True:
            return qs.filter(is_ausschuss=True)
        else:
            return qs


admin.site.register(User, CustomUserAdmin)
admin.site.register(Bewerber)
