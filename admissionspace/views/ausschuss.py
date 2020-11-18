from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from admissionspace.models import Bewerbung


class ApplicationListView(ListView):
    model = Bewerbung
    template_name = 'admissionspace/admission/application_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['approved_admissions'] = len(Bewerbung.objects.filter(status='A'))
        context['pending_admissions'] = len(Bewerbung.objects.filter(status='P'))
        context['declined_admissions'] = len(Bewerbung.objects.filter(status='D'))
        return context


class AdmissionApplicationUpdateView(UpdateView):
    model = Bewerbung
    template_name = 'admissionspace/admission/application_admission.html'
    fields = ['status']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enrolment_capacity'] = 200 - len(Bewerbung.objects.filter(status='A'))
        return context

    def form_valid(self, form):
        object = form.save(commit=False)
        if len(Bewerbung.objects.filter(status='A')) >= 200:
            return redirect('application_list')
        else:
            object.save()
            return redirect('application_list')
