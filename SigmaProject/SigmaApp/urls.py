from django.urls import path
from SigmaApp.views import *

urlpatterns = [
    path('index/', index, name="Home"),
    
    path('aboutMe/', aboutMe, name="About Me"),
    # Create
    path('createTeachers/', create_teacher, name="Create Teacher"),
    path('createClients/', create_client, name="Create Client"),
    path('createActivities/', create_activity, name="Create Activities"),
    path('createPlaces/', create_place, name="Create Place"),
    # Read
    path('readTeachers/', read_teacher, name="Read Teacher"),
    # Update
    # Delete
]
