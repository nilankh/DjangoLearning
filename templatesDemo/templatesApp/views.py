from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    myDict = {"name":"Nilank Nikhil"}

    return render(request, 'templatesApp/firstTemplate.html', context=myDict)

def renderEmployee(request):
    myDict = {"id":123, "name":"Nilank Nikhil", "salary":1000000}
    return render(request,'templatesApp/employeeTemplate.html', myDict)