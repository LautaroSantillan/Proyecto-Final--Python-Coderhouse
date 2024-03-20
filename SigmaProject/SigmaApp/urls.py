from django.urls import path
from SigmaApp.views import *
from . import views
from django.conf.urls import handler404

# Manejador para la página de error 404
handler404 = views.error_404

urlpatterns = [
    path('index/', index, name="Home"),
    # Pages
    path('aboutMe/', aboutMe, name="About Me"),
    path('404/', views.error_404, name='error_404'),
    # User Autenticado
    path('signup/', register_user, name="Registrarse"),
    path("login/", login_user, name="Iniciar Sesion"),
    path("logout/", logout_user, name="Cerrar Sesion"),
    # Create
    path('createTeachers/', create_teacher, name="Create Teacher"),
    path('createClients/', create_client, name="Create Client"),
    path('createActivities/', create_activity, name="Create Activities"),
    path('createPlaces/', create_place, name="Create Place"),
    # Read
    path('readTeachers/', read_teacher, name="Read Teacher"),
    path('readClients/', read_client, name="Read Client"),
    path('readPlaces/', read_place, name="Read Place"),
    # Update
    path('updateClients/<infoClient>/', update_client, name="Update Client"),
    path('updatePlaces/<infoPlace>/', update_place, name="Update Place"),
    # Delete
    path('deleteClients/<infoClient>/', delete_client, name="Delete Client"),
    path('deletePlaces/<infoPlace>/', delete_place, name="Delete Place"),
]