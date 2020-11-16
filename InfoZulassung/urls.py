"""InfoZulassung URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accountspace.views import BewerberSignUpView, CustomLoginView
import admissionspace.views.bewerber as bewerber_views

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('signup/', BewerberSignUpView.as_view(), name='bewerber_signup'),

    # Application Views - Bewerbersicht
    path('applicant/myapplications', bewerber_views.ApplicantIndexView.as_view(),
         name='applicant_index'),

    path('applicant/createuniversitydegree', bewerber_views.UniversityDegreeCreateView.as_view(),
         name='create_uni_degree'),
    path('applicant/updateuniversitydegree/<slug:pk>/', bewerber_views.UniversityDegreeUpdateView.as_view(),
         name='update_uni_degree'),
    path('applicant/deleteuniversitydegree/<slug:pk>/', bewerber_views.UniversityDegreeDeleteView.as_view(),
         name='delete_uni_degree'),

    path('applicant/createschooldegree', bewerber_views.SchoolDegreeCreateView.as_view(),
         name='create_school_degree'),
    path('applicant/updateschooldegree/<slug:pk>/', bewerber_views.SchoolDegreeUpdateView.as_view(),
         name='update_school_degree'),
    path('applicant/deleteschooldegree/<slug:pk>/', bewerber_views.SchoolDegreeDeleteView.as_view(),
         name='delete_school_degree'),

    path('applicant/createworkexp', bewerber_views.WorkExperienceCreateView.as_view(),
         name='create_work_exp'),
    path('applicant/updateworkexp/<slug:pk>/', bewerber_views.WorkExperienceUpdateView.as_view(),
         name='update_work_exp'),
    path('applicant/deleteworkexp/<slug:pk>/', bewerber_views.WorkExperienceDeleteView.as_view(),
         name='delete_work_exp'),

    path('applicant/createapplication', bewerber_views.BewerbungCreateView.as_view(),
         name='create_bewerbung'),
    path('applicant/updateapplication/<slug:pk>/', bewerber_views.BewerbungUpdateView.as_view(),
         name='update_bewerbung'),
    path('applicant/deleteapplication/<slug:pk>/', bewerber_views.BewerbungDeleteView.as_view(),
         name='delete_bewerbung'),
]
