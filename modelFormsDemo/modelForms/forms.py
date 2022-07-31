from attr import fields
from django import forms
from modelForms import models
from modelForms.models import Project

class ProjectForm(forms.ModelForm):
    # Meta inner class which will tell dajngo which model that it should be used in this form and also the fields that should be included from that model
    class Meta:
        models = Project
        fields = '__all__'
