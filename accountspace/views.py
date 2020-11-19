from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.views import LoginView

from django.contrib.auth import login

from admissionspace.decorators import bewerber_required
from .models import User, Bewerber
from .forms import BewerberSignUpForm, CustomLoginForm, BewerberUpdateForm


# Create your views here.
class BewerberSignUpView(CreateView):
    model = User
    form_class = BewerberSignUpForm
    template_name = 'accountspace/signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('applicant_index')


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'accountspace/signin.html'

    def get_success_url(self):
        if self.request.user.is_bewerber:
            success_url = 'applicant_index'
        elif self.request.user.is_ausschuss:
            success_url = 'application_list'
        return reverse(success_url)

@method_decorator([login_required, bewerber_required], name='dispatch')
class BewerberUpdateView(UpdateView):
    model = Bewerber
    form_class = BewerberUpdateForm
    template_name = 'accountspace/changeuserdata.html'
    success_url = reverse_lazy('applicant_index')

    def get_form(self, *args, **kwargs):
        form = super(BewerberUpdateView, self).get_form(*args, **kwargs)
        form.queryset = Bewerber.objects.filter(user_id=self.request.user.id)
        return form
