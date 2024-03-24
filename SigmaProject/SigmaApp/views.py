from django.shortcuts import render
from SigmaApp.models import *
from SigmaApp.forms import *

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    place = Place.objects.all()
    return render(request, "index.html", {"place": place})

def aboutMe(request):
    return render(request, "aboutMe.html")

def aboutUs(request):
    return render(request, "aboutUs.html")

def error_404(request, exception):
    return render(request, "error404.html", status=404)

# User Autenticado
def register_user(request):
    if request.method == "POST":
        form = userRegister(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "index.html", {"message": "El usuario ha sido creado exitosamente!"})
    else:
        form = userRegister()

    return render(request, "account-signin/register.html", {"form": form})

@login_required
def update_user(request):
    user = request.user
    if request.method == "POST":
        form = userUpdate(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            user.email = info["email"]
            user.set_password = info["password1"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
            user.save()
            return render(request, "index.html")
    else:
        form = userUpdate(initial={
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        })
    
    return render(request, "account-signin/update.html", {"form": form})

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            infoDic = form.cleaned_data
            user = authenticate(username = infoDic["username"], password = infoDic["password"])
            if user is not None:
                login(request, user)
                return render(request, "index.html", {"message": f"Bienvenido {user}!"})
        else:
            return render(request, "index.html", {"message": "Credenciales incorrectas"})
    else:
        form = AuthenticationForm()

    return render(request, "account-signin/login.html", {"form": form})

@login_required
def add_avatar(request):
    if request.method == "POST":
        form = avatarForm(request.POST, request.FILES)
        if form.is_valid():
            currentUser = User.objects.get(username=request.user)
            avatar = Avatar(user=currentUser, img=form.cleaned_data["img"])
            avatar.save()
            return render(request, "index.html")
    else: 
        form = avatarForm()

    return render(request, "account-signin/addAvatar.html", {"form": form})

def logout_user(request):
    logout(request)
    return render(request, "index.html", {"message": "Has cerrado la sesión!"})

#CRUD Teacher
@login_required
def create_teacher(request):
    if request.method == "POST":
        forms = TeacherForm(request.POST)
        if forms.is_valid():
            infoDic = forms.cleaned_data
            teacher = Teacher(
                name=infoDic["name"], 
                lastname=infoDic["lastname"],
                email=infoDic["email"],
                role=infoDic["role"],
            )
            teacher.save()
            return render(request, "index.html")                      
    else: 
        forms= TeacherForm()
    
    return render(request, "teachers/createTeacher.html", {"form": forms})

def read_teacher(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers/readTeacher.html", {"teachers": teachers})

@login_required    
def update_teacher(request, infoTeacher):
    teacher = Teacher.objects.get(id=infoTeacher)
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            infoDic = form.cleaned_data
            teacher.name = infoDic["name"]
            teacher.lastname = infoDic["lastname"]
            teacher.email = infoDic["email"]
            teacher.role = infoDic["role"]
            teacher.save()
            return render(request, "index.html")
    else:
        form = TeacherForm(initial={
            "name": teacher.name,
            "lastname": teacher.lastname,
            "email": teacher.email,
            "role": teacher.role,
        })

    return render(request, "teachers/updateTeacher.html", {"form": form})

@login_required
def delete_teacher(request, infoTeacher):
    teacher = Teacher.objects.get(id=infoTeacher)
    teacher.delete()
    return render(request, "index.html")

#CRUD Client
def create_client(request):
    if request.method == "POST":
        forms = ClientForm(request.POST)
        if forms.is_valid():
            infoDic = forms.cleaned_data
            client = Client(
                name=infoDic["name"], 
                lastname=infoDic["lastname"],
                email=infoDic["email"],
                age=infoDic["age"],
                birthday=infoDic["birthday"],
            )
            client.save()
            return render(request, "index.html")                      
    else: 
        forms= ClientForm()
    
    return render(request, "clients/createClient.html", {"form": forms})

def read_client(request):
    clients = Client.objects.all()
    return render(request, "clients/readClient.html", {"clients": clients})

@login_required
def update_client(request, infoClient):
    client = Client.objects.get(id=infoClient)
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            infoDic = form.cleaned_data
            client.name = infoDic["name"]
            client.lastname = infoDic["lastname"]
            client.email = infoDic["email"]
            client.age = infoDic["age"]
            client.birthday = infoDic["birthday"]
            client.save()
            return render(request, "index.html")
    else:
        form = ClientForm(initial={
            "name": client.name,
            "lastname": client.lastname,
            "email": client.email,
            "age": client.age,
            "birthday": client.birthday,
        })

    return render(request, "clients/updateClient.html", {"form": form})

@login_required
def delete_client(request, infoClient):
    client = Client.objects.get(id=infoClient)
    client.delete()
    return render(request, "index.html")

#CRUD Activity
@login_required
def create_activity(request):
    if request.method == "POST":
        forms = ActivityForm(request.POST)
        if forms.is_valid():
            infoDic = forms.cleaned_data
            activity = Activity(
                name=infoDic["name"], 
                day=infoDic["day"],
                hour=infoDic["hour"],
            )
            activity.save()
            return render(request, "index.html")                      
    else: 
        forms= ActivityForm()
    
    return render(request, "activities/createActivity.html", {"form": forms})

def read_activity(request):
    activities = Activity.objects.all()
    return render(request, "activities/readActivity.html", {"activities": activities})

@login_required
def update_activity(request, infoActivity):
    activity = Activity.objects.get(id=infoActivity)
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            infoDic = form.cleaned_data
            activity.name = infoDic["name"]
            activity.day = infoDic["day"]
            activity.hour = infoDic["hour"]
            activity.save()
            return render(request, "index.html")
    else:
        form = ActivityForm(initial={
            "name": activity.name,
            "day": activity.day,
            "hour": activity.hour,
        })

    return render(request, "activities/updateActivity.html", {"form": form})

@login_required
def delete_activity(request, infoActivity):
    activity = Activity.objects.get(id=infoActivity)
    activity.delete()
    return render(request, "index.html")

#CRUD Place
@login_required
def create_place(request):
    if request.method == "POST":
        forms = PlaceForm(request.POST)
        if forms.is_valid():
            infoDic = forms.cleaned_data
            place = Place(
                street=infoDic["street"], 
                number=infoDic["number"],
                city=infoDic["city"],
                province=infoDic["province"],
            )
            place.save()
            return render(request, "index.html")                      
    else: 
        forms= PlaceForm()
    
    return render(request, "places/createPlace.html", {"form": forms})

def read_place(request):
    places = Place.objects.all()
    return render(request, "places/readPlace.html", {"places": places})

@login_required
def update_place(request, infoPlace):
    place = Place.objects.get(id=infoPlace)
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            infoDic = form.cleaned_data
            place.street = infoDic["street"]
            place.number = infoDic["number"]
            place.city = infoDic["city"]
            place.province = infoDic["province"]
            place.save()
            return render(request, "index.html")
    else:
        form = PlaceForm(initial={
            "street": place.street,
            "number": place.number,
            "city": place.city,
            "province": place.province,
        })

    return render(request, "places/updatePlace.html", {"form": form})

@login_required
def delete_place(request, infoPlace):
    place = Place.objects.get(id=infoPlace)
    place.delete()
    return render(request, "index.html")
