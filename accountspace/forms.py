from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction

from .models import User, Bewerber


class BewerberSignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.EmailInput(attrs={
            'type': 'email',
            'class': 'form-control custom-form-control',
            'placeholder': 'Email'
        })
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'type': 'password',
            'class': 'form-control custom-form-control',
            'placeholder': 'Passwort'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'type': 'password',
            'class': 'form-control custom-form-control',
            'placeholder': 'Passwort bestätigen'
        })

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control custom-form-control',
        'placeholder': 'Vorname'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control custom-form-control',
        'placeholder': 'Nachname'
    }))
    street = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control custom-form-control',
        'placeholder': 'Straße & Hausnummer'
    }))
    city = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control custom-form-control',
        'placeholder': 'Stadt'
    }))
    post_code = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control custom-form-control',
        'placeholder': 'PLZ'
    }))

    phone = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control custom-form-control',
        'placeholder': 'Telefon'
    }))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_bewerber = True
        user.last_name = self.cleaned_data.get('last_name')
        user.first_name = self.cleaned_data.get('first_name')
        user.email = self.cleaned_data.get('username')
        user.save()

        Bewerber.objects.create(
            user=user,
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            street=self.cleaned_data.get('street'),
            post_code=self.cleaned_data.get('post_code'),
            city=self.cleaned_data.get('city'),
            email=self.cleaned_data.get('username'),
            phone=self.cleaned_data.get('phone')
        )
        return user


class BewerberUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BewerberUpdateForm, self).__init__(*args, **kwargs)

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control custom-form-control',
        'placeholder': 'Vorname'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control custom-form-control',
        'placeholder': 'Nachname'
    }))
    street = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control custom-form-control',
        'placeholder': 'Straße & Hausnummer'
    }))
    city = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control custom-form-control',
        'placeholder': 'Stadt'
    }))
    post_code = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control custom-form-control',
        'placeholder': 'PLZ'
    }))

    phone = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control custom-form-control',
        'placeholder': 'Telefon'
    }))

    class Meta(UserCreationForm.Meta):
        model = Bewerber
        fields = ['first_name', 'last_name', 'street', 'city', 'post_code', 'phone']


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.EmailInput(attrs={

        'type': 'email',
        'class': 'form-control custom-form-control',
        'placeholder': 'Email'

    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={

        'type': 'password',
        'class': 'form-control form-control custom-form-control',
        'placeholder': 'Passwort'

    }))
