from operator import truediv
from typing import Self
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    about=models.CharField(max_length=500)
    city=models.TextField(blank=True,null=True)
    state=models.TextField(blank=True,null=True)
    district=models.TextField(blank=True,null=True)
    profil_picture=models.ImageField(upload_to='profiles/',blank=True,null=True)


    def __str__(self):
        return self.user.username


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.degree}"

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.company

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Certification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    certificate_name = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    issue_date = models.DateField()

    def __str__(self):
        return self.certificate_name

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50)

    def __str__(self):
        return self.skill_name

class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    achievement_date = models.DateField()

    def __str__(self):
        return self.title


class Language(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50)

    def __str__(self):
        return self.language

class Award(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    award_name = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    award_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.award_name

class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    publication_date = models.DateField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    provider = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    completion_date = models.DateField()

    def __str__(self):
        return self.course_name
    