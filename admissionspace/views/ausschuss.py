from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView

from admissionspace.decorators import ausschuss_required
from admissionspace.models import Bewerbung, Recommendation


@method_decorator([login_required, ausschuss_required], name='dispatch')
class ApplicationListView(ListView):
    model = Bewerbung
    template_name = 'admissionspace/admission/application_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['approved_admissions'] = len(Bewerbung.objects.filter(status='A'))
        context['pending_admissions'] = len(Bewerbung.objects.filter(status='P'))
        context['declined_admissions'] = len(Bewerbung.objects.filter(status='D'))
        return context


@method_decorator([login_required, ausschuss_required], name='dispatch')
class AdmissionApplicationUpdateView(UpdateView):
    model = Bewerbung
    template_name = 'admissionspace/admission/application_admission.html'
    fields = ['status']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enrolment_capacity'] = 200 - len(Bewerbung.objects.filter(status='A'))
        user_id = Bewerbung.objects.filter(id=self.kwargs['pk']).values('bewerber_id')
        context['recommendations'] = Recommendation.objects.filter(bewerber=user_id[0]['bewerber_id'])
        return context

    def form_valid(self, form):
        object = form.save(commit=False)
        if len(Bewerbung.objects.filter(status='A')) >= 200:
            return redirect('application_list')
        else:
            object.save()
            return redirect('application_list')
