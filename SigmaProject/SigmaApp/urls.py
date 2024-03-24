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
    path('aboutUs', aboutUs, name="About Us"),
    path('404/', views.error_404, name='error_404'),
    # User Autenticado
    path('signup/', register_user, name="Registrarse"),
    path('login/', login_user, name="Iniciar Sesion"),
    path('update/', views.update_user, name="Actualizar Usuario"),
    path('addAvatar/', add_avatar, name="Agregar Avatar"),
    path('logout/', logout_user, name="Cerrar Sesion"),
    # Create
    path('createTeachers/', create_teacher, name="Create Teacher"),
    path('createClients/', create_client, name="Create Client"),
    path('createActivities/', create_activity, name="Create Activity"),
    path('createPlaces/', create_place, name="Create Place"),
    # Read
    path('readTeachers/', read_teacher, name="Read Teacher"),
    path('readClients/', read_client, name="Read Client"),
    path('readActivities/', read_activity, name="Read Activity"),
    path('readPlaces/', read_place, name="Read Place"),
    # Update
    path('updateTeachers/<infoTeacher>/', update_teacher, name="Update Teacher"),
    path('updateClients/<infoClient>/', update_client, name="Update Client"),
    path('updateActivities/<infoActivity>/', update_activity, name="Update Activity"),
    path('updatePlaces/<infoPlace>/', update_place, name="Update Place"),
    # Delete
    path('deleteTeachers/<infoTeacher>/', delete_teacher, name="Delete Teacher"),
    path('deleteClients/<infoClient>/', delete_client, name="Delete Client"),
    path('deleteActivities/<infoActivity>/', delete_activity, name="Delete Activity"),
    path('deletePlaces/<infoPlace>/', delete_place, name="Delete Place"),
]