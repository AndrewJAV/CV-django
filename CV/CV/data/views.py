from django.shortcuts import render
from .models import Person, Skill, Aptitude, Education, Language, Contact

def CV(request):
    
    person = Person.objects.first()
    aptitudes = Aptitude.objects.all()
    contacts = Contact.objects.all()
    languages = Language.objects.all()
    skills = Skill.objects.all()
    education = Education.objects.all()
    
    context = {
        'person':person,
        'contacts':contacts,
        'languages':languages,
        'aptitudes':aptitudes,
        'skills':skills,
        'education':education,
    }
    
    return render(request, 'CV.html', context)

# Create your views here.
