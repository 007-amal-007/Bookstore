from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]
        widgets={
            'first_name':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your First Name"}),
            'last_name':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your Last Name"}),
            'email':forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter your Email Id"}),
            'username':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your Username"}),
            'password1':forms.PasswordInput(attrs={"class": 'form-control', "placeholder": "Password from numbers and letters of the Latin alphabet"}),
            'password2':forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirmation'})
        }
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class OrderForm(forms.Form):
    address=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))