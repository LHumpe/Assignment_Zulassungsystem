from django.db import models
from accountspace.models import User


# Create your models here.
class UniversityDegree(models.Model):
    candidate = models.ForeignKey(User, on_delete=models.CASCADE)

    university_name = models.CharField(max_length=128)
    name_of_degree = models.CharField(max_length=128)

    DEGREE_CHOICES = (
        ('msc', 'Master of Science'),
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

    def __str__(self):
        return "{} {} {}".format(self.name_of_degree, self.type_of_degree, self.university_name)


class WorkExperience(models.Model):
    candidate = models.ForeignKey(User, on_delete=models.CASCADE)

    company_name = models.CharField(max_length=128)
    starting_date = models.DateField()
    end_date = models.DateField()
    employment_relationship = models.CharField(max_length=128)
    industry = models.CharField(max_length=128)
    supervisor = models.CharField(max_length=128)
    specialisation = models.CharField(max_length=128)
    task_description = models.TextField()
    company_address = models.TextField()
    avg_weekly_working_time = models.IntegerField()

    def __str__(self):
        return "{} {}".format(self.company_name, self.employment_relationship)


class SchoolDegree(models.Model):
    candidate = models.ForeignKey(User, on_delete=models.CASCADE)

    school_name = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    type_of_degree = models.CharField(max_length=128)
    graduation_date = models.DateField()
    starting_date = models.DateField()
    avg_score = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return "{} {}".format(self.school_name, self.type_of_degree)


class Bewerbung(models.Model):
    bewerber = models.ForeignKey(User, on_delete=models.CASCADE)
    uni_degrees = models.ManyToManyField(UniversityDegree, blank=True)
    school_degrees = models.ManyToManyField(SchoolDegree)
    work_experiences = models.ManyToManyField(WorkExperience, blank=True)

    STATUS_CHOICES = (
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('D', 'Declined'),
    )
    status = models.CharField(max_length=1, default='P', choices=STATUS_CHOICES)

    date_of_entry = models.DateTimeField(auto_created=True)

    def __str__(self):
        return 'User:{}'.format(self.bewerber)


class Recommendation(models.Model):
    bewerber = models.ForeignKey(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    job_position = models.CharField(max_length=40, default='')
    company_name = models.CharField(max_length=128)
    company_address = models.TextField()
    email = models.EmailField(default='')
    phone = models.CharField(max_length=12, default='')

    available_from = models.TimeField()
    available_until = models.TimeField()

    recommendation_letter = models.TextField()

    def __str__(self):
        return 'User:{} NR:{}'.format(self.bewerber, self.id)
