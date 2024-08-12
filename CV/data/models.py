from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    
class Contact(models.Model):
    CONTACT_TYPES = [
        ('phone', 'Phone'),
        ('email','Email'),
        ('github','Github'),
        ('instagram','Instagram'),
        ('linkedin','Linkedin'),
        ('adress','Adress'),
    ]
    
    kind = models.CharField(max_length=20, choices=CONTACT_TYPES)
    value = models.CharField(max_length=255)

class Language(models.Model):
    name = models.CharField(max_length=20)
    proficiency = models.IntegerField()

class Aptitude(models.Model):
    name = models.CharField(max_length=50)
    
class Skill(models.Model):
    value = models.TextField()
    
class Education(models.Model):
    institution = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    start_date = models.CharField(max_length=5, null=False)
    end_date = models.CharField(max_length=10, default='Presente')

    
    
