# urls.py in your app (e.g., degree_checklist)

from django.urls import path
from .views import create_course,create_degree_program,degree_program_list,model_list,course_list,student_detail,degree_detail,api_degree_detail,DegreeDetailView,admin_interface

urlpatterns = [
    path('create_degree/', create_degree_program, name='create_degree_program'),
    path('create_degree_course/', create_course, name='create_course'),
    path('degree_program_view/', degree_program_list, name='degree_program_list'),
    path('course_list/', course_list, name='course_list'),
    path('students_view/<int:student_id>/', student_detail, name='student_detail'),
    # path('degree_view/', degree_view, name='degree_view'),
    path('degree_detail_view/<int:program_id>/', degree_detail, name='degree_detail'),
    # path('degrees/<int:program_id>/', degree_view, name='degree_view'),
    path('api/degrees/<int:program_id>/', DegreeDetailView.as_view(), name='degree-detail-api'),
    path('admin/', admin_interface, name='admin_interface'),
]