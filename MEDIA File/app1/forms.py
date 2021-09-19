from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUser(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields =['username','email']

    # def save(self,commit=True):
    #     user=super(RegisterUser,self).save(commit=False)
    #     user.email = self.changed_data.get("email")
    #     if commit:
    #         user.save()
    #     return user

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError(u'This email address is already registered.')
        return email