from django import forms
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
    
class ActivityForm(forms.Form):
    name = forms.CharField(max_length=40)
    day = forms.CharField(max_length=10)
    hour = forms.IntegerField()
    
class PlaceForm(forms.Form):
    street = forms.CharField(max_length=40)
    number = forms.IntegerField()
    city = forms.CharField(max_length=50)
    province = forms.CharField(max_length=50)