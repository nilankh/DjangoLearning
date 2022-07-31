from django.shortcuts import render
from modelForms.forms import ProjectForm
from modelForms.forms import Project

# Create your views here.
def index(request):
    return render(request, 'modelForms/index.html')

def listProjects(request):
    projectList = Project.objects.all()
    return render(request, 'modelForms/listProjects.html', {'projects':projectList})


def addProject(request):
    form = ProjectForm()
    if(form.method == 'POST'):
        form = MovieForm(request.POST)
        if(form.is_valid()):
            form.save()
        return index(request)

    return render(request, 'modelForms/addProject.html', {'form':form})