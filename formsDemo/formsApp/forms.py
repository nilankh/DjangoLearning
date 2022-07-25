from django import forms

class UserRegistrationForm(forms.Form):
    GENDER = [('male','MALE'),('female','FEMALE')]
    firstName= forms.CharField()
    lastName= forms.CharField()
    email= forms.CharField()
    gender = forms.CharField(widget=forms.Select(choices=GENDER))
    password = forms.CharField(widget=forms.PasswordInput)
    ssn = forms.IntegerField()

    # def clean_firstName(self):
    #     inputFirstName = self.cleaned_data['firstName']
    #     if len(inputFirstName) > 20:
    #         raise forms.ValidationError('The max length of firstName is 20 characters')
    #     return inputFirstName

    # def clean_email(self):
    #     inputEmail = self.cleaned_data['email']
    #     if inputEmail.find('@')== -1:
    #         raise forms.ValidationError('The email shoudl contain @')
    #     return inputEmail

# Learning about single clean method
    def clean(self):
        user_cleaned_data = super().clean()
        inputFirstName = user_cleaned_data['firstName']
        inputEmail = user_cleaned_data['email']
        if len(inputFirstName) > 20:
            raise forms.ValidationError('The max length of firstName is 20 characters')
        if inputEmail.find('@')== -1:
            raise forms.ValidationError('The email shoudl contain @')
        



