from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from ..models import UniversityDegree, SchoolDegree, WorkExperience, Bewerbung
import datetime


class ApplicantIndexView(TemplateView):
    model = UniversityDegree
    template_name = 'admissionspace/applications/applicant_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['universitydegrees'] = UniversityDegree.objects.filter(candidate=self.request.user)
        context['workexperience'] = WorkExperience.objects.filter(candidate=self.request.user)
        context['schooldegrees'] = SchoolDegree.objects.filter(candidate=self.request.user)
        context['bewerbung'] = Bewerbung.objects.filter(bewerber=self.request.user)
        return context


class UniversityDegreeCreateView(CreateView):
    model = UniversityDegree
    template_name = 'admissionspace/applications/university_degreee.html'
    fields = ['university_name', 'name_of_degree', 'type_of_degree', 'specialisation', 'graduation_date',
              'starting_date', 'no_of_semesters', 'avg_score']

    def form_valid(self, form):
        object = form.save(commit=False)
        object.candidate = self.request.user
        object.save()
        return redirect('applicant_index')


class UniversityDegreeUpdateView(UpdateView):
    model = UniversityDegree
    template_name = 'admissionspace/applications/university_degreee.html'
    fields = ['university_name', 'name_of_degree', 'type_of_degree', 'specialisation', 'graduation_date',
              'starting_date', 'no_of_semesters', 'avg_score']
    success_url = reverse_lazy('applicant_index')


class UniversityDegreeDeleteView(DeleteView):
    model = UniversityDegree
    template_name = 'admissionspace/applications/university_degreee.html'
    success_url = reverse_lazy('applicant_index')


class SchoolDegreeCreateView(CreateView):
    model = SchoolDegree
    template_name = 'admissionspace/applications/school_degree.html'
    fields = ['school_name', 'city', 'type_of_degree', 'graduation_date', 'starting_date', 'avg_score']

    def form_valid(self, form):
        object = form.save(commit=False)
        object.candidate = self.request.user
        object.save()
        return redirect('applicant_index')


class SchoolDegreeUpdateView(UpdateView):
    model = SchoolDegree
    template_name = 'admissionspace/applications/school_degree.html'
    fields = ['school_name', 'city', 'type_of_degree', 'graduation_date', 'starting_date', 'avg_score']
    success_url = reverse_lazy('applicant_index')


class SchoolDegreeDeleteView(DeleteView):
    model = SchoolDegree
    template_name = 'admissionspace/applications/school_degree.html'
    success_url = reverse_lazy('applicant_index')


class WorkExperienceCreateView(CreateView):
    model = WorkExperience
    template_name = 'admissionspace/applications/work_experience.html'
    fields = ['company_name', 'company_address', 'industry', 'starting_date', 'end_date', 'employment_relationship',
              'supervisor', 'specialisation', 'task_description', 'avg_weekly_working_time']

    def form_valid(self, form):
        object = form.save(commit=False)
        object.candidate = self.request.user
        object.save()
        return redirect('applicant_index')


class WorkExperienceUpdateView(UpdateView):
    model = WorkExperience
    template_name = 'admissionspace/applications/work_experience.html'
    fields = ['company_name', 'company_address', 'industry', 'starting_date', 'end_date', 'employment_relationship',
              'supervisor', 'specialisation', 'task_description', 'avg_weekly_working_time']
    success_url = reverse_lazy('applicant_index')


class WorkExperienceDeleteView(DeleteView):
    model = WorkExperience
    template_name = 'admissionspace/applications/work_experience.html'
    success_url = reverse_lazy('applicant_index')


class BewerbungCreateView(CreateView):
    model = Bewerbung
    template_name = 'admissionspace/applications/bewerbung.html'
    fields = ['uni_degrees', 'school_degrees', 'work_experiences']

    def form_valid(self, form):
        object = form.save(commit=False)
        object.bewerber = self.request.user
        object.date_of_entry = datetime.datetime.now()
        object.save()
        return redirect('update_uni_degree')


class BewerbungUpdateView(UpdateView):
    model = Bewerbung
    template_name = 'admissionspace/applications/bewerbung.html'
    fields = ['uni_degrees', 'school_degrees', 'work_experiences']
    success_url = reverse_lazy('applicant_index')


class BewerbungDeleteView(DeleteView):
    model = Bewerbung
    template_name = 'admissionspace/applications/bewerbung.html'
    success_url = reverse_lazy('applicant_index')
