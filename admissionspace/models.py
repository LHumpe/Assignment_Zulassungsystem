from django.db import models
from accountspace.models import Bewerber


# Create your models here.
class UniversityDegree(models.Model):
    candidate = models.ForeignKey(Bewerber, on_delete=models.CASCADE)

    university_name = models.CharField(max_length=128)
    name_of_degree = models.CharField(max_length=128)

    DEGREE_CHOICES = (
        ('bsc', 'Master of Science'),
        ('ma', 'Master of Arts'),
        ('bsc', 'Bachelor of Science'),
        ('ba', 'Bachelor of Arts'),
    )

    type_of_degree = models.CharField(max_length=3, choices=DEGREE_CHOICES)
    specialisation = models.CharField(max_length=128)
    graduation_date = models.DateField()
    starting_date = models.DateField()
    no_of_semesters = models.IntegerField()
    avg_score = models.DecimalField(max_digits=2, decimal_places=1)


class WorkExperience(models.Model):
    candidate = models.ForeignKey(Bewerber, on_delete=models.CASCADE)

    company_name = models.CharField(max_length=128)
    starting_year = models.DateField()
    end_year = models.DateField()
    employment_relationship = models.CharField(max_length=128)
    industry = models.CharField(max_length=128)
    supervisor = models.CharField(max_length=128)
    specialisation = models.CharField(max_length=128)
    task_description = models.TextField()
    company_address = models.TextField()
    avg_weekly_working_time = models.IntegerField()


class SchoolDegrees(models.Model):
    candidate = models.ForeignKey(Bewerber, on_delete=models.CASCADE)

    school_name = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    type_of_degree = models.CharField(max_length=128)
    graduation_year = models.DateField()
    starting_year = models.DateField()
    avg_score = models.DecimalField(max_digits=2, decimal_places=1)


class Bewerbung(models.Model):
    bewerber = models.ForeignKey(Bewerber, on_delete=models.CASCADE)
    uni_degrees = models.ManyToManyField(UniversityDegree)
    school_degrees = models.ManyToManyField(SchoolDegrees)
    work_experiences = models.ManyToManyField(WorkExperience)

    STATUS_CHOICES = (
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('D', 'Declined'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    date_of_entry = models.DateTimeField(auto_created=True)
