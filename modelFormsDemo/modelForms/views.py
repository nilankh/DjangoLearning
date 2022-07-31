from django.shortcuts import render
from modelForms.forms import ProjectForm
from modelForms.forms import Project

# Create your views here.
def index(request):
    return render(request, 'modelForms/index.html')

def listProjects(request):
    projectList = Project.objects.all()
    return render(request, 'modelForms/listProjects.html', {'projects':projectList})

    