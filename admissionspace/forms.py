from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.shortcuts import redirect
from .models import UniversityDegree, SchoolDegree, WorkExperience, Bewerbung, Recommendation

from .models import User


class UniversityDegreeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UniversityDegreeForm, self).__init__(*args, **kwargs)

        self.fields['university_name'].label = "Universitätsname"
        self.fields['name_of_degree'].label = "Studiengang"
        self.fields['type_of_degree'].label = "Abschlussbezeichnung"
        self.fields['specialisation'].label = "Spezialisierung"
        self.fields['graduation_date'].label = "Abschlussdatum"
        self.fields['starting_date'].label = "Startdatum"
        self.fields['no_of_semesters'].label = "Anzahl der benötigten Semester"
        self.fields['avg_score'].label = "Notenschnitt"


        self.fields['university_name'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control custom-form-control',
            'placeholder': 'Universität'
        })
        self.fields['name_of_degree'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control custom-form-control',
            'placeholder': 'Studiengang'
        })
        self.fields['type_of_degree'].widget = forms.Select(attrs={
            'type': 'text',
            'class': 'form-control custom-form-control',
            'placeholder': 'Abschluss'
        }, choices=UniversityDegree.DEGREE_CHOICES)
        self.fields['specialisation'].widget = forms.TextInput(attrs={
            'type': 'select',
            'class': 'form-control custom-form-control',
            'placeholder': 'Spezialisierung'
        })
        self.fields['graduation_date'].widget = forms.TextInput(attrs={
            'type': 'date',
            'class': 'form-control custom-form-control',
            'placeholder': 'Datum des Abschlusses'
        })
        self.fields['starting_date'].widget = forms.TextInput(attrs={
            'type': 'date',
            'class': 'form-control custom-form-control',
            'placeholder': 'Startdatum'
        })
        self.fields['no_of_semesters'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control custom-form-control',
            'placeholder': 'Anzahl Semester'
        })
        self.fields['avg_score'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control custom-form-control',
            'placeholder': 'Notenschnitt'
        })

    class Meta:
        model = UniversityDegree
        fields = ["university_name", "name_of_degree", "type_of_degree", "specialisation", "graduation_date",
                  "starting_date", "no_of_semesters", "avg_score"]


class SchoolDegreeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SchoolDegreeForm, self).__init__(*args, **kwargs)

        self.fields['school_name'].label = "Schule"
        self.fields['city'].label = "Stadt"
        self.fields['type_of_degree'].label = "Abschlussbezeichnung"
        self.fields['graduation_date'].label = "Datum des Abschlusses"
        self.fields['starting_date'].label = "Einschulungsdatum"
        self.fields['avg_score'].label = "Notenschnitt"


        self.fields['school_name'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control custom-form-control',
            'placeholder': 'Schule'
        })
        self.fields['city'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control custom-form-control',
            'placeholder': 'Stadt'
        })
        self.fields['type_of_degree'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control custom-form-control',
            'placeholder': 'Abschluss'
        })
        self.fields['graduation_date'].widget = forms.TextInput(attrs={
            'type': 'date',
            'class': 'form-control custom-form-control',
            'placeholder': 'Datum des Abschlusses'
        })
        self.fields['starting_date'].widget = forms.TextInput(attrs={
            'type': 'date',
            'class': 'form-control custom-form-control',
            'placeholder': 'Startdatum'
        })
        self.fields['avg_score'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control custom-form-control',
            'placeholder': 'Notenschnitt'
        })

    class Meta:
        model = SchoolDegree
        fields = ["school_name", "city", "type_of_degree", "graduation_date", "starting_date",
                  "avg_score"]


class WorkExperienceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(WorkExperienceForm, self).__init__(*args, **kwargs)

        self.fields['company_name'].label = "Unternehmen"
        self.fields['end_date'].label = "Enddatum"
        self.fields['starting_date'].label = "Startdatum"
        self.fields['employment_relationship'].label = "Position"
        self.fields['industry'].label = "Branche"
        self.fields['supervisor'].label = "Ansprechpartner"
        self.fields['specialisation'].label = "Spezialisierung"
        self.fields['task_description'].label = "Beschreibung"
        self.fields['avg_weekly_working_time'].label = "Arbeitszeit in Std./Woche"
        self.fields['company_address'].label = "Anschrift des Unternehmens"



        self.fields['company_name'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control custom-form-control',
            'placeholder': 'Unternehmen'
        })
        self.fields['end_date'].widget = forms.TextInput(attrs={
            'type': 'date',
            'class': 'form-control custom-form-control',
            'placeholder': 'Enddatum'
        })
        self.fields['starting_date'].widget = forms.TextInput(attrs={
            'type': 'date',
            'class': 'form-control custom-form-control',
            'placeholder': 'Startdatum'
        })
        self.fields['employment_relationship'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control custom-form-control',
            'placeholder': 'Position im Unternehmen'
        })
        self.fields['industry'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control custom-form-control',
            'placeholder': 'Branche'
        })
        self.fields['supervisor'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control custom-form-control',
            'placeholder': 'Ansprechpartner'
        })
        self.fields['specialisation'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control custom-form-control',
            'placeholder': 'Spezialisierung'
        })
        self.fields['task_description'].widget = forms.Textarea(attrs={
            'type': 'multi',
            'class': 'form-control custom-form-control',
            'placeholder': 'Beschreibung der Tätigkeit'
        })
        self.fields['company_address'].widget = forms.Textarea(attrs={
            'type': 'multi',
            'class': 'form-control custom-form-control',
            'placeholder': 'Anschrift des Unternehmens'
        })
        self.fields['avg_weekly_working_time'].widget = forms.TextInput(attrs={
            'type': 'integer',
            'class': 'form-control custom-form-control',
            'placeholder': 'Durchschnittliche wöchentliche Arbeitszeit'
        })

    class Meta:
        model = WorkExperience
        fields = ["company_name", "starting_date", "end_date", "employment_relationship", "industry",
                  "supervisor", "specialisation", "task_description", "company_address", "avg_weekly_working_time"]


class BewerbungForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BewerbungForm, self).__init__(*args, **kwargs)
        self.fields['uni_degrees'].label = "Universitätsabschlüsse"
        self.fields['school_degrees'].label = "Schulabschlüsse"
        self.fields['work_experiences'].label = "Arbeitserfahrungen"

        self.fields['uni_degrees'].widget = forms.CheckboxSelectMultiple(attrs={
            'type': 'checkbox',
            'class': 'form-group custom-no-dots',

        })
        self.fields['school_degrees'].widget = forms.CheckboxSelectMultiple(attrs={
            'type': 'checkbox',
            'class': 'form-group custom-no-dots',
        })
        self.fields['work_experiences'].widget = forms.CheckboxSelectMultiple(attrs={
            'type': 'checkbox',
            'class': 'form-group custom-no-dots',
        })

    class Meta:
        model = Bewerbung
        fields = ["uni_degrees", "school_degrees", "work_experiences", ]



class RecommendationCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RecommendationCreateForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].label = "Vorname"
        self.fields['last_name'].label = "Nachname"
        self.fields['job_position'].label = "Position"
        self.fields['company_name'].label = "Name des Unternehmens"
        self.fields['company_address'].label = "Anschrift des Unternehmens"
        self.fields['email'].label = "E-Mail"
        self.fields['phone'].label = "Telefonnummer"
        self.fields['available_from'].label = "Erreichbar ab"
        self.fields['available_until'].label = "Erreichbar bis"
        self.fields['recommendation_letter'].label = "Empfehlungsschreiben"

        self.fields['first_name'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control custom-form-control',
            'placeholder': 'Vorname'
        })
        self.fields['last_name'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control custom-form-control',
            'placeholder': 'Nachname'
        })
        self.fields['job_position'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control custom-form-control',
            'placeholder': 'Position'
        })
        self.fields['company_name'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control custom-form-control',
            'placeholder': 'Name des Unternehmens'
        })
        self.fields['company_address'].widget = forms.Textarea(attrs={
            'type': 'multi',
            'class': 'form-control custom-form-control',
            'placeholder': 'Anschrift des Unternehmens'
        })
        self.fields['email'].widget = forms.EmailInput(attrs={
            'type': 'text',
            'class': 'form-control custom-form-control',
            'placeholder': 'E-Mail'
        })
        self.fields['phone'].widget = forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control custom-form-control',
            'placeholder': 'Telefonnummer'
        })
        self.fields['available_from'].widget = forms.TextInput(attrs={
            'type': 'time',
            'class': 'form-control custom-form-control',
            'placeholder': 'Geben Sie hier bitte eine Uhrzeit an ab der Sie erreichbar sind'
        })
        self.fields['available_until'].widget = forms.TextInput(attrs={
            'type': 'time',
            'class': 'form-control custom-form-control',
            'placeholder': 'Geben Sie hier bitte eine Uhrzeit an bis zu der Sie erreichbar sind'
        })

        self.fields['recommendation_letter'].widget = forms.Textarea(attrs={
            'type': 'multi',
            'class': 'form-control custom-form-control',
            'placeholder': 'Bitte schreiben Sie in dieses Feld ihr Empfehlungsschreiben für den Bewerber'
        })

    class Meta:
        model = Recommendation
        fields = ["first_name", "last_name", "job_position", "company_name", "company_address",
                  "email", "phone", "available_from", "available_until", "recommendation_letter"]