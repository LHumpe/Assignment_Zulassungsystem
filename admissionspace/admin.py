from django.contrib import admin
from .models import UniversityDegree, SchoolDegree, WorkExperience, Bewerbung, Recommendation


class BewerbungAdmin(admin.ModelAdmin):
    list_display = ('id', 'bewerber', 'status',)
    fieldsets = (
        (None, {
            'fields': ('bewerber',)
        }),
        ('Bewerbungsstatus ändern', {
            'classes': ('wide',),
            'fields': ('status',),
        }),
    )
    readonly_fields = ['bewerber']


class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('id', 'bewerber',)

    readonly_fields = ['bewerber']


class SchoolDegreeAdmin(admin.ModelAdmin):
    list_display = ('id', 'candidate')


class UniversityDegreeAdmin(admin.ModelAdmin):
    list_display = ('id', 'candidate')


class WorkExperienceDegreeAdmin(admin.ModelAdmin):
    list_display = ('id', 'candidate')


admin.site.register(UniversityDegree, UniversityDegreeAdmin)
admin.site.register(SchoolDegree, SchoolDegreeAdmin)
admin.site.register(WorkExperience, WorkExperienceDegreeAdmin)
admin.site.register(Bewerbung, BewerbungAdmin)
admin.site.register(Recommendation, RecommendationAdmin)
