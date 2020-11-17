from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from admissionspace.models import Bewerbung


class ApplicationListView(ListView):
    model = Bewerbung
    template_name = 'admissionspace/admission/application_list.html'




class AdmissionApplicationUpdateView(UpdateView):
    model = Bewerbung
    template_name = 'admissionspace/admission/application_admission.html'
    fields='__all__'
    success_url = reverse_lazy('application_list')
