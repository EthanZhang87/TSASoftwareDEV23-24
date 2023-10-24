from django.db import models

# Create your models here.

class Tutor(models.Model):
    class Subject(models.TextChoices):
        MATH = 'Math'
        SCIENCE = 'Science'
        SOCIAL_STUDIES = 'Social Studies'
        ELA = 'Ela'

    class Levels(models.TextChoices):
        MATH = 'Math'
        SCIENCE = 'Science'
        SOCIAL_STUDIES = 'Social Studies'
        ELA = 'Ela'

    name = models.CharField(max_length=100)
    bio = models.TextField()
    subject = models.CharField(max_length=20, choices = Subject.choices, null=False, blank=False)
    level = models.CharField(max_length=20, choices = Levels.choices, null=False, blank=False)
    email = models.EmailField(max_length=100)
