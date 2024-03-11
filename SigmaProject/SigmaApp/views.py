from django.shortcuts import render
from SigmaApp.models import *
from SigmaApp.forms import *
# Create your views here.
def index(request):
    place = Place.objects.all()
    return render(request, "index.html", {"place": place})

#CRUD Teacher
def create_teacher(request):
    if request.method == "POST": #Cuando apreto el btn submit
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
    
#CRUD Client
def create_client(request):
    if request.method == "POST": #Cuando apreto el btn submit
        forms = ClientForm(request.POST)
        if forms.is_valid():
            infoDic = forms.cleaned_data
            client = Client(
                name=infoDic["name"], 
                lastname=infoDic["lastname"],
                email=infoDic["email"],
                age=infoDic["age"],
            )
            client.save()
            return render(request, "index.html")                      
    else: 
        forms= ClientForm()
    
    return render(request, "clients/createClient.html", {"form": forms})

def read_client(request):
    if request.GET: 
        name = request.GET["name"] 
        clients = Client.objects.filter(name__icontains=name)
        message = f"Estamos buscando al cliente {name}..."
        #return render(request, "teachers/readTeacher.html", {"clients": clients, "message": message})
    
    #return render(request, "teachers/readTeacher.html")

#CRUD Activity
def create_activity(request):
    if request.method == "POST": #Cuando apreto el btn submit
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

#CRUD Place
def create_place(request):
    if request.method == "POST": #Cuando apreto el btn submit
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