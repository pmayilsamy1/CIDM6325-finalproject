# Degree Checklist Web Application Documentation
Table of Contents
1. [Introduction](#Introduction)
2. [Installation](#Installation)
3. [Usage](#Usage)
4. [Application Structure](#Application-Structure)
5. [API Endpoints](#API-Endpoints)
6. [Deploying apps in Amazon Web Sevice](#Deploying-apps-in-Amazon-Web-Sevice)


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
![Image](https://github.com/pmayilsamy1/CIDM6325-finalproject/blob/main/screenshots/screenshot1.jpg)
![Image](https://github.com/pmayilsamy1/CIDM6325-finalproject/blob/main/screenshots/screenshot2.jpg)

### 3. Usage
#### Admin Interface
The admin interface allows you to manage degree programs. Navigate to http://127.0.0.1:8000/degreechecklistview/admin/ to view and modify degree programs.
![Image](https://github.com/pmayilsamy1/CIDM6325-finalproject/blob/main/screenshots/screenshot3.jpg)

#### Creating Degree Programs and Courses
- Access the degree creation form at http://127.0.0.1:8000/degreechecklistview/create_degree/
![Image](https://github.com/pmayilsamy1/CIDM6325-finalproject/blob/main/screenshots/screenshot4.jpg)

- Access the course creation form at http://127.0.0.1:8000/degreechecklistview/create_degree_course/
![Image](https://github.com/pmayilsamy1/CIDM6325-finalproject/blob/main/screenshots/screenshot5.jpg)

#### Viewing Lists
- Degree Program List: http://127.0.0.1:8000/degreechecklistview/degree_program_view/
![Image](https://github.com/pmayilsamy1/CIDM6325-finalproject/blob/main/screenshots/screenshot6.jpg)

- Course List: http://127.0.0.1:8000/degreechecklistview/course_list/
![Image](https://github.com/pmayilsamy1/CIDM6325-finalproject/blob/main/screenshots/screenshot7.jpg)

#### Student and Degree Details
- Student Detail: http://127.0.0.1:8000/degreechecklistview/students_view/1/
![Image](https://github.com/pmayilsamy1/CIDM6325-finalproject/blob/main/screenshots/screenshot8.jpg)

- Degree Detail: http://127.0.0.1:8000/degreechecklistview/degree_detail_view/1/
![Image](https://github.com/pmayilsamy1/CIDM6325-finalproject/blob/main/screenshots/screenshot9.jpg)

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
![Image](https://github.com/pmayilsamy1/CIDM6325-finalproject/blob/main/screenshots/screenshot10.jpg)

### 6. Deploying apps in Amazon Web Sevice

#### 1. Set Up AWS Account
- Signed up for AWS account & logged into AWS console to 
access the AWS Management Console.
- Navigate to the EC2 Dashboard and create a new EC2 instance (virtual server).
#### 2. Configure EC2 Instance
- Choose an Amazon Machine Image (AMI) for your instance. 
- Select an instance type based on your project requirements.
- Configure instance details, including the number of instances, network settings, and IAM role if needed.
- Add storage to your instance. Ensure you have enough storage for your Django project and databases.
- Configure security groups to allow inbound traffic on ports 80 (HTTP) and 22 (SSH) as well as 8000 port for Django 

![Image](https://github.com/pmayilsamy1/CIDM6325-finalproject/blob/main/screenshots/screenshot11.jpg)

![Image](https://github.com/pmayilsamy1/CIDM6325-finalproject/blob/main/screenshots/screenshot12.jpg)

#### 3. Connect to EC2 Instance
Use an SSH client to connect to your EC2 instance. You can use the private key generated during the instance creation process.

ssh -i ~/Downloads/myawskey.pem ec2-user@3.21.41.119

#### 4. Install Required Software on EC2 Instance
- Update the package list:

        sudo yum update -y

- Install Python and other dependencies:

        sudo yum install python3 python3-pip git -y
- Clone your Django project from your GitHub repository:


        git clone https://github.com/pmayilsamy1/CIDM6325-finalproject.git
- Navigate to the project directory and install project dependencies:

        cd degree-checklist
        pip3 install -r requirements.txt

#### 5. Collect Static Files
-   Run the following command to collect static files:

        python3 manage.py collectstatic

#### 6. Install and Configure Gunicorn
- Install Gunicorn (a production-ready WSGI server for Django):
        pip3 install gunicorn
-   Test Gunicorn to ensure it's working:


    gunicorn finalProject .wsgi:application
#### 7. Configure Nginx as a Reverse Proxy
- Install Nginx:
        sudo yum install nginx -y

Configure Nginx as a reverse proxy by creating a new Nginx configuration file.

bash 
```
server {
    listen 80;
    server_name your-domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        root /path/to/your/project;
    }

    location / {
        include proxy_params;
        proxy_pass http://127.0.0.1:8000;
    }
}
```
-   Restart Nginx:

        sudo systemctl restart nginx


#### 8 Run Gunicorn in the Background
- Run Gunicorn in the background, using the Nginx configuration file created earlier:

        gunicorn --workers 3 degree_checklist.wsgi:application

![Image](https://github.com/pmayilsamy1/CIDM6325-finalproject/blob/main/screenshots/screenshot13.jpg)

create superuser using python manage.py createsuperuser


![Image](https://github.com/pmayilsamy1/CIDM6325-finalproject/blob/main/screenshots/screenshot14.jpg)

![Image](https://github.com/pmayilsamy1/CIDM6325-finalproject/blob/main/screenshots/screenshot15.jpg)
