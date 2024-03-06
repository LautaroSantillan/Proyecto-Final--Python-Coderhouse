# README - SigmaApp

## Introduction
This is a brief README for the SigmaApp application. It provides an overview of the functionalities and a guide to finding them in the source code.

## Features and Test Order

1. **Home (Index)**
   - URL: /index/
   - View: `index` in `views.py`
   - Template: `index.html`
   - Description: Home page of the application.

2. **Create Teacher**
   - URL: /createTeachers/
   - View: `create_teacher` in `views.py`
   - Template: `teachers/createTeacher.html`
   - Description: Allows creating a new teacher.

3. **Create Client**
   - URL: /createClients/
   - View: `create_client` in `views.py`
   - Template: `clients/createClient.html`
   - Description: Allows creating a new client.

4. **Create Activity**
   - URL: /createActivities/
   - View: `create_activity` in `views.py`
   - Template: `activities/createActivity.html`
   - Description: Allows creating a new activity.

5. **Create Place**
   - URL: /createPlaces/
   - View: `create_place` in `views.py`
   - Template: `places/createPlace.html`
   - Description: Allows creating a new place.

6. **Read Teacher**
   - URL: /readTeachers/
   - View: `read_teacher` in `views.py`
   - Template: `teachers/readTeacher.html`
   - Description: Allows searching and displaying teachers.

## Usage
- To run the application, make sure you have Django installed and configured correctly.
- Run the Django development server using the command `python manage.py runserver`.
- Navigate to the different URLs mentioned above to test the functionalities.
