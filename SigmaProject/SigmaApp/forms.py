from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from SigmaApp.models import Avatar
# Create your forms here.
class TeacherForm(forms.Form):
    name = forms.CharField(max_length=40)
    lastname = forms.CharField(max_length=50)
    email = forms.EmailField()
    role = forms.CharField(max_length=40)
    
class ClientForm(forms.Form):
    name = forms.CharField(max_length=40)
    lastname = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField()
    birthday = forms.DateField()
    
class ActivityForm(forms.Form):
    name = forms.CharField(max_length=40)
    day = forms.CharField(max_length=10)
    hour = forms.IntegerField()
    
class PlaceForm(forms.Form):
    street = forms.CharField(max_length=40)
    number = forms.IntegerField()
    city = forms.CharField(max_length=50)
    province = forms.CharField(max_length=50)

class userRegister(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Ingrese nuevamente la contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

class userUpdate(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Ingrese nuevamente la contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]

class avatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["img"]
