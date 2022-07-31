from django.shortcuts import render, redirect
from fbCrud.forms import StudentForm
from fbvApp.models import Student

# Create your views here.
def getStudent(request):
    students = Student.objects.all()
    return render(request, 'fbvApp/index.html', {'students':students})

def createStudent(request):
    form = StudentForm()
    if(request.method == 'POST'):
        form = StudentForm(request.POST)
        if(form.is_valid):
            form.save()
        return redirect('/')
    return render(request, 'fbvApp/create.html', {'form':form})

def deleteStudent(request, id):
    student = Student.objects.get(id = id)

    student.delete()

    return redirect('/')
