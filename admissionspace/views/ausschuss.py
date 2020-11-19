from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView

from admissionspace.decorators import ausschuss_required
from admissionspace.models import Bewerbung

@method_decorator([login_required, ausschuss_required], name='dispatch')
class ApplicationListView(ListView):
    model = Bewerbung
    template_name = 'admissionspace/admission/application_list.html'



@method_decorator([login_required, ausschuss_required], name='dispatch')
class AdmissionApplicationUpdateView(UpdateView):
    model = Bewerbung
    template_name = 'admissionspace/admission/application_admission.html'
    fields=['status']
    success_url = reverse_lazy('application_list')
