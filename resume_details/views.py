from django.shortcuts import render
from django.http import HttpResponse
import mimetypes
from .models import BasicDetails, Skills, Experiance, Extra, Project, Certification, Education 
#Create your views here.

def details(request):
    basic = BasicDetails.objects.all()
    skills = Skills.objects.all()
    projects = Project.objects.all()
    experiance = Experiance.objects.all()
    extra = Extra.objects.all()
    education = Education.objects.all()
    certificates = Certification.objects.all()

    context = {'basic':basic,'skills':skills,'projects':projects,'experiance':experiance,'extra':extra,'education':education,'certificates':certificates}
    return render(request,'index.html',context) 

