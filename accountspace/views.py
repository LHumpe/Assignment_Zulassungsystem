from django.shortcuts import render, redirect,reverse
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView

from django.contrib.auth import login
from .models import User, Bewerber
from .forms import BewerberSignUpForm, CustomLoginForm


# Create your views here.
class BewerberSignUpView(CreateView):
    model = User
    form_class = BewerberSignUpForm
    template_name = 'accountspace/signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('bewerber_signup')


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'accountspace/signin.html'

    def get_success_url(self):
        if self.request.user.is_bewerber:
            success_url = 'applicant_index'
        elif self.request.user.is_ausschuss:
            success_url = 'Hier_DIE_URL_Fuer_den_AUSSCHUSS_EINTRAGEN'
        return reverse(success_url)
