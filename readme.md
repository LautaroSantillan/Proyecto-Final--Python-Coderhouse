# README - SigmaApp

## Introduction
This README provides an overview of the SigmaApp project, a gym landing page management system. It outlines the project's functionalities, models, URLs, and provides instructions on how to run and use the application.

## Objective
The objective of SigmaApp is to provide a comprehensive platform for managing various aspects of a gym landing page. Users can create, read, update, and delete (CRUD) teachers, clients, activities, and places.

## Models

### Teacher
- **Fields:**
  - Name (CharField)
  - Lastname (CharField)
  - Email (EmailField)
  - Role (CharField)

### Client
- **Fields:**
  - Name (CharField)
  - Lastname (CharField)
  - Email (EmailField)
  - Age (IntegerField)
  - Birthday (DateField)

### Activity
- **Fields:**
  - Name (CharField)
  - Day (CharField)
  - Hour (IntegerField)

### Place
- **Fields:**
  - Street (CharField)
  - Number (IntegerField)
  - City (CharField)
  - Province (CharField)

### Avatar
- **Fields:**
  - User (OneToOneField)
  - Img (ImageField)

## CRUD URLs
Below are the CRUD URLs for managing various entities in SigmaApp:

```python
urlpatterns = [
    # Home
    path('index/', index, name="Home"),
    
    # Pages
    path('aboutMe/', aboutMe, name="About Me"),
    path('aboutUs', aboutUs, name="About Us"),
    path('404/', views.error_404, name='error_404'),

    # User Authentication
    path('signup/', register_user, name="Registrarse"),
    path('login/', login_user, name="Iniciar Sesion"),
    path('update/', views.update_user, name="Actualizar Usuario"),
    path('addAvatar/', add_avatar, name="Agregar Avatar"),
    path('logout/', logout_user, name="Cerrar Sesion"),

    # CRUD Operations
    path('createTeachers/', create_teacher, name="Create Teacher"),
    path('createClients/', create_client, name="Create Client"),
    path('createActivities/', create_activity, name="Create Activity"),
    path('createPlaces/', create_place, name="Create Place"),

    path('readTeachers/', read_teacher, name="Read Teacher"),
    path('readClients/', read_client, name="Read Client"),
    path('readActivities/', read_activity, name="Read Activity"),
    path('readPlaces/', read_place, name="Read Place"),

    path('updateTeachers/<infoTeacher>/', update_teacher, name="Update Teacher"),
    path('updateClients/<infoClient>/', update_client, name="Update Client"),
    path('updateActivities/<infoActivity>/', update_activity, name="Update Activity"),
    path('updatePlaces/<infoPlace>/', update_place, name="Update Place"),

    path('deleteTeachers/<infoTeacher>/', delete_teacher, name="Delete Teacher"),
    path('deleteClients/<infoClient>/', delete_client, name="Delete Client"),
    path('deleteActivities/<infoActivity>/', delete_activity, name="Delete Activity"),
    path('deletePlaces/<infoPlace>/', delete_place, name="Delete Place"),
] 
```

## Superuser Credentials
- **Username:** lautaro (superuser) - **Password:** Python88

- **Username:** Lautaro (superuser) - **Password:** Lolita10

## Technology Stack

### Front-End
- HTML 5
- CSS 3
- JavaScript ES6
- Bootstrap 5.3.3

### Back-End
- Python 3.11
- Django 5.0.2

## Usage
- To run the application, ensure you have Django installed and configured correctly.
- Run the Django development server using the command `python manage.py runserver`.
- Navigate to the different URLs mentioned below to test the functionalities.
