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
from accountspace.views import BewerberSignUpView, CustomLoginView, BewerberUpdateView
from django.contrib.auth import views as auth_views
import admissionspace.views.bewerber as bewerber_views
import admissionspace.views.ausschuss as ausschuss_views

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('signup/', BewerberSignUpView.as_view(), name='bewerber_signup'),
    path('signout/', auth_views.LogoutView.as_view(next_page='login'), name='signout'),

    # Application Views - Bewerbersicht
    path('changeuserdata/<slug:pk>/', BewerberUpdateView.as_view(), name='bewerber_update'),
    path('myapplications', bewerber_views.ApplicantIndexView.as_view(),
         name='applicant_index'),

    path('createuniversitydegree', bewerber_views.UniversityDegreeCreateView.as_view(),
         name='create_uni_degree'),
    path('updateuniversitydegree/<slug:pk>/', bewerber_views.UniversityDegreeUpdateView.as_view(),
         name='update_uni_degree'),
    path('deleteuniversitydegree/<slug:pk>/', bewerber_views.UniversityDegreeDeleteView.as_view(),
         name='delete_uni_degree'),

    path('createschooldegree', bewerber_views.SchoolDegreeCreateView.as_view(),
         name='create_school_degree'),
    path('updateschooldegree/<slug:pk>/', bewerber_views.SchoolDegreeUpdateView.as_view(),
         name='update_school_degree'),
    path('deleteschooldegree/<slug:pk>/', bewerber_views.SchoolDegreeDeleteView.as_view(),
         name='delete_school_degree'),

    path('createworkexp', bewerber_views.WorkExperienceCreateView.as_view(),
         name='create_work_exp'),
    path('updateworkexp/<slug:pk>/', bewerber_views.WorkExperienceUpdateView.as_view(),
         name='update_work_exp'),
    path('deleteworkexp/<slug:pk>/', bewerber_views.WorkExperienceDeleteView.as_view(),
         name='delete_work_exp'),

    path('createapplication', bewerber_views.BewerbungCreateView.as_view(),
         name='create_bewerbung'),
    path('viewapplication/<slug:pk>/', bewerber_views.BewerbungDetailView.as_view(),
         name='detail_bewerbung'),
    path('updateapplication/<slug:pk>/', bewerber_views.BewerbungUpdateView.as_view(),
         name='update_bewerbung'),
    path('deleteapplication/<slug:pk>/', bewerber_views.BewerbungDeleteView.as_view(),
         name='delete_bewerbung'),

    path('myapplications/recommend/<slug:pk>/', bewerber_views.RecommendationCreateView.as_view(), name='recommend'),
    path('myapplications/view_recommend/<slug:pk>/', bewerber_views.RecommendationDetailView.as_view(),
         name='detail_recommendation'),

    # Admission views
    path('viewapplications', ausschuss_views.ApplicationListView.as_view(),
         name='application_list'),
    path('approveapplication/<slug:pk>/', ausschuss_views.AdmissionApplicationUpdateView.as_view(),
         name='approve_application'),

    # password-reset routes
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='accountspace/password_reset.html'), name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accountspace/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accountspace/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accountspace/password_reset_complete.html'),
         name='password_reset_complete'),
]
