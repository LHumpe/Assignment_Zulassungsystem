from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, DetailView

from accountspace.models import Bewerber, User
from ..models import UniversityDegree, SchoolDegree, WorkExperience, Bewerbung, Recommendation
from ..decorators import bewerber_required, user_required
from ..forms import UniversityDegreeForm, SchoolDegreeForm, WorkExperienceForm, BewerbungForm, RecommendationCreateForm
import datetime


@method_decorator([login_required, bewerber_required], name='dispatch')
class ApplicantIndexView(TemplateView):
    model = UniversityDegree
    template_name = 'admissionspace/applications/applicant_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['universitydegrees'] = UniversityDegree.objects.filter(candidate=self.request.user)
        context['workexperience'] = WorkExperience.objects.filter(candidate=self.request.user)
        context['schooldegrees'] = SchoolDegree.objects.filter(candidate=self.request.user)
        context['bewerbung'] = Bewerbung.objects.filter(bewerber=self.request.user)
        context['account_information'] = Bewerber.objects.filter(user=self.request.user)
        context['recommendations'] = Recommendation.objects.filter(bewerber=self.request.user)
        context['recommendation_link'] = '/recommend/{}/'.format(self.request.user.id)
        return context


@method_decorator([login_required, bewerber_required], name='dispatch')
class UniversityDegreeCreateView(CreateView):
    model = UniversityDegree
    template_name = 'admissionspace/applications/university_degreee.html'
    form_class = UniversityDegreeForm

    def form_valid(self, form):
        object = form.save(commit=False)
        object.candidate = self.request.user
        object.save()
        return redirect('applicant_index')


@method_decorator([login_required, bewerber_required], name='dispatch')
class UniversityDegreeUpdateView(UpdateView):
    model = UniversityDegree
    template_name = 'admissionspace/applications/university_degreee.html'
    form_class = UniversityDegreeForm
    success_url = reverse_lazy('applicant_index')


@method_decorator([login_required, bewerber_required], name='dispatch')
class UniversityDegreeDeleteView(DeleteView):
    model = UniversityDegree
    template_name = 'admissionspace/applications/university_degreee.html'
    success_url = reverse_lazy('applicant_index')


@method_decorator([login_required, bewerber_required], name='dispatch')
class SchoolDegreeCreateView(CreateView):
    model = SchoolDegree
    template_name = 'admissionspace/applications/school_degree.html'
    form_class = SchoolDegreeForm

    def form_valid(self, form):
        object = form.save(commit=False)
        object.candidate = self.request.user
        object.save()
        return redirect('applicant_index')


@method_decorator([login_required, bewerber_required], name='dispatch')
class SchoolDegreeUpdateView(UpdateView):
    model = SchoolDegree
    template_name = 'admissionspace/applications/school_degree.html'
    form_class = SchoolDegreeForm
    success_url = reverse_lazy('applicant_index')


@method_decorator([login_required, bewerber_required], name='dispatch')
class SchoolDegreeDeleteView(DeleteView):
    model = SchoolDegree
    template_name = 'admissionspace/applications/school_degree.html'
    success_url = reverse_lazy('applicant_index')


@method_decorator([login_required, bewerber_required], name='dispatch')
class WorkExperienceCreateView(CreateView):
    model = WorkExperience
    template_name = 'admissionspace/applications/work_experience.html'
    form_class = WorkExperienceForm

    def form_valid(self, form):
        object = form.save(commit=False)
        object.candidate = self.request.user
        object.save()
        return redirect('applicant_index')


@method_decorator([login_required, bewerber_required], name='dispatch')
class WorkExperienceUpdateView(UpdateView):
    model = WorkExperience
    template_name = 'admissionspace/applications/work_experience.html'
    form_class = WorkExperienceForm
    success_url = reverse_lazy('applicant_index')


@method_decorator([login_required, bewerber_required], name='dispatch')
class WorkExperienceDeleteView(DeleteView):
    model = WorkExperience
    template_name = 'admissionspace/applications/work_experience.html'
    success_url = reverse_lazy('applicant_index')


@method_decorator([login_required, bewerber_required], name='dispatch')
class BewerbungCreateView(CreateView):
    model = Bewerbung
    template_name = 'admissionspace/applications/bewerbung.html'
    form_class = BewerbungForm

    def get_form(self, *args, **kwargs):
        form = super(BewerbungCreateView, self).get_form(*args, **kwargs)
        form.fields['uni_degrees'].queryset = UniversityDegree.objects.filter(candidate__bewerber=self.request.user.id)
        form.fields['school_degrees'].queryset = SchoolDegree.objects.filter(candidate__bewerber=self.request.user.id)
        form.fields['work_experiences'].queryset = WorkExperience.objects.filter(candidate=self.request.user.id)
        return form

    def form_valid(self, form):
        object = form.save(commit=False)
        object.bewerber = self.request.user
        object.date_of_entry = datetime.datetime.now()
        object.save()
        form.save_m2m()
        return redirect('applicant_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account_information'] = Bewerber.objects.filter(user=self.request.user)
        return context


@method_decorator([login_required, bewerber_required], name='dispatch')
class BewerbungUpdateView(UpdateView):
    model = Bewerbung
    template_name = 'admissionspace/applications/bewerbung.html'
    form_class = BewerbungForm
    success_url = reverse_lazy('applicant_index')

    def get_form(self, *args, **kwargs):
        form = super(BewerbungUpdateView, self).get_form(*args, **kwargs)
        form.fields['uni_degrees'].queryset = UniversityDegree.objects.filter(candidate__bewerber=self.request.user.id)
        form.fields['school_degrees'].queryset = SchoolDegree.objects.filter(candidate__bewerber=self.request.user.id)
        form.fields['work_experiences'].queryset = WorkExperience.objects.filter(candidate=self.request.user.id)
        return form


@method_decorator([login_required, bewerber_required], name='dispatch')
class BewerbungDetailView(DetailView):
    model = Bewerbung
    template_name = 'admissionspace/applications/bewerbung_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recommendations'] = Recommendation.objects.filter(bewerber=self.request.user)
        return context


@method_decorator([login_required, bewerber_required], name='dispatch')
class BewerbungDeleteView(DeleteView):
    model = Bewerbung
    template_name = 'admissionspace/applications/bewerbung_delete.html'
    success_url = reverse_lazy('applicant_index')


class RecommendationCreateView(CreateView):
    model = Recommendation
    template_name = 'admissionspace/applications/recommendation_create.html'
    form_class = RecommendationCreateForm
    success_url = reverse_lazy('applicant_index')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.bewerber = User.objects.get(id=self.kwargs['pk'])
        object.save()
        return redirect('applicant_index')

@method_decorator([login_required, user_required], name='dispatch')
class RecommendationDetailView(DetailView):
    model = Recommendation
    template_name = 'admissionspace/applications/recommendation_detail.html'



