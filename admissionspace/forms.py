from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.shortcuts import redirect
from .models import UniversityDegree, SchoolDegree, WorkExperience, Bewerbung

from .models import User


class UniversityDegreeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UniversityDegreeForm, self).__init__(*args, **kwargs)
        self.fields['university_name'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Universität'
        })
        self.fields['name_of_degree'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Studiengang'
        })
        self.fields['type_of_degree'].widget = forms.Select(attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Abschluss'
        }, choices=UniversityDegree.DEGREE_CHOICES)
        self.fields['specialisation'].widget = forms.TextInput(attrs={
            'type': 'select',
            'class': 'form-control',
            'placeholder': 'Spezialisierung'
        })
        self.fields['graduation_date'].widget = forms.TextInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'placeholder': 'Datum des Abschlusses'
        })
        self.fields['starting_date'].widget = forms.TextInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'placeholder': 'Startdatum'
        })
        self.fields['no_of_semesters'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Anzahl Semester'
        })
        self.fields['avg_score'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Numerus clausus'
        })

    class Meta:
        model = UniversityDegree
        fields = ["university_name", "name_of_degree", "type_of_degree", "specialisation", "graduation_date",
                  "starting_date", "no_of_semesters", "avg_score"]


class SchoolDegreeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SchoolDegreeForm, self).__init__(*args, **kwargs)
        self.fields['school_name'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Schule'
        })
        self.fields['city'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Stadt'
        })
        self.fields['type_of_degree'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Abschluss'
        })
        self.fields['graduation_date'].widget = forms.TextInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'placeholder': 'Datum des Abschlusses'
        })
        self.fields['starting_date'].widget = forms.TextInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'placeholder': 'Startdatum'
        })
        self.fields['avg_score'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Numerus clausus'
        })

    class Meta:
        model = SchoolDegree
        fields = ["school_name", "city", "type_of_degree", "graduation_date", "starting_date",
                  "avg_score"]


class WorkExperienceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(WorkExperienceForm, self).__init__(*args, **kwargs)
        self.fields['company_name'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Firma'
        })
        self.fields['end_date'].widget = forms.TextInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'placeholder': 'Enddatum'
        })
        self.fields['starting_date'].widget = forms.TextInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'placeholder': 'Startdatum'
        })
        self.fields['employment_relationship'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Beschäftigung'
        })
        self.fields['industry'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Branche'
        })
        self.fields['supervisor'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Ansprechpartner'
        })
        self.fields['specialisation'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Spezialisierung'
        })
        self.fields['task_description'].widget = forms.Textarea(attrs={
            'type': 'multi',
            'class': 'form-control',
            'placeholder': 'Beschreibung der Tätigkeit'
        })
        self.fields['company_address'].widget = forms.Textarea(attrs={
            'type': 'multi',
            'class': 'form-control',
            'placeholder': 'Anschrift der Firma'
        })
        self.fields['avg_weekly_working_time'].widget = forms.TextInput(attrs={
            'type': 'integer',
            'class': 'form-control',
            'placeholder': 'Durchschnittliche wöchentliche Arbeitszeit'
        })

    class Meta:
        model = WorkExperience
        fields = ["company_name", "starting_date", "end_date", "employment_relationship", "industry",
                  "supervisor", "specialisation", "task_description", "company_address", "avg_weekly_working_time"]


class BewerbungForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BewerbungForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Bewerbung
        fields = ["uni_degrees", "school_degrees", "work_experiences", ]
        widgets = {
            "uni_degrees": forms.SelectMultiple(attrs={
                'type': 'SelectMultiple',
                'class': 'form-control',
                'placeholder': 'Abschluss'}),
            "school_degrees": forms.SelectMultiple(attrs={
                'type': 'SelectMultiple',
                'class': 'form-control',
                'placeholder': 'Abschluss'}),
            "work_experiences": forms.SelectMultiple(attrs={
                'type': 'SelectMultiple',
                'class': 'form-control',
                'placeholder': 'Abschluss'})

        }
