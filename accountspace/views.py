from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import login
from .models import User, Bewerber
from .forms import BewerberSignUpForm

# Create your views here.
class BewerberSignUpView(CreateView):
    model = User
    form_class = BewerberSignUpForm
    template_name = 'accountspace/signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('bewerber_signup')
