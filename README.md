# Degree Checklist Web Application Documentation
Table of Contents
1. [Introduction](#Introduction)
2. [Installation](#Installation)
3. [Usage](#Usage)
4. [Application Structure](#Application-Structure)
5. [API Endpoints](#API-Endpoints)


### 1. Introduction
The Degree Checklist Web Application is a Django-based system designed to manage degree programs, courses, and student enrollments. This documentation provides a comprehensive guide on the installation, usage, and structure of the application.

### 2. Installation
#### Prerequisites
-   Python 3.x
-   Django
-   Django Rest Framework

#### Steps
1. Clone the Repository:

``` bash
git clone https://github.com/pmayilsamy1/CIDM6325-finalproject
cd degree-checklist
```
2. Install Dependencies:

``` bash
pip install -r requirements.txt
```
3. Apply Migrations:

``` bash
python manage.py migrate
```
4. Create Superuser (Admin):
``` bash
python manage.py createsuperuser
```
5. Run the Development Server:
``` bash
python manage.py runserver
```

Open your browser and go to http://localhost:8000/admin to log in with the superuser credentials.
![Image](screenshot1.jpg)
![Image](screenshot2.jpg)

### 3. Usage
#### Admin Interface
The admin interface allows you to manage degree programs. Navigate to http://127.0.0.1:8000/degreechecklistview/admin/ to view and modify degree programs.
![Image](screenshot3.jpg)

#### Creating Degree Programs and Courses
- Access the degree creation form at http://127.0.0.1:8000/degreechecklistview/create_degree/
![Image](screenshot4.jpg)

- Access the course creation form at http://127.0.0.1:8000/degreechecklistview/create_degree_course/
![Image](screenshot5.jpg)

#### Viewing Lists
- Degree Program List: http://127.0.0.1:8000/degreechecklistview/degree_program_view/
![Image](screenshot6.jpg)

- Course List: http://127.0.0.1:8000/degreechecklistview/course_list/
![Image](screenshot7.jpg)

#### Student and Degree Details
- Student Detail: http://127.0.0.1:8000/degreechecklistview/students_view/1/
![Image](screenshot8.jpg)

- Degree Detail: http://127.0.0.1:8000/degreechecklistview/degree_detail_view/1/
![Image](screenshot9.jpg)

### 4. Application Structure

The application follows a standard Django structure:

degree_checklist/: Django project settings.
degree_checklist/urls.py: URL configurations for the app.
degree_checklist/views.py: Views and API endpoints.
degree_checklist/templates/: HTML templates.
degree_checklist/models.py: Database models.
degree_checklist/forms.py: Django forms for data input.
degree_checklist/admin.py: Admin interface customization.
requirements.txt: List of Python dependencies.
###  5. API Endpoints
The application includes API endpoints for retrieving degree details.

Degree Detail API: http://localhost:8000/api/degrees/{program_id}/
![Image](screenshot10.jpg)