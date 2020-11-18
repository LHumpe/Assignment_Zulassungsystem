from django.contrib import admin
from .models import UniversityDegree, SchoolDegree, WorkExperience, Bewerbung

# Register your models here.
admin.site.register(UniversityDegree)
admin.site.register(SchoolDegree)
admin.site.register(WorkExperience)
admin.site.register(Bewerbung)
