# views.py

from django.shortcuts import render, redirect,get_object_or_404
from .forms import DegreeProgramForm, CourseForm,DegreeProgram, Course
from .models import Student, EnrollsIn
from .models import DegreeProgram, Department, Course, EnrollsIn, CoreRequirement, Includes, Requires, Has, DegreespecificRequirement, IncludesDegreespecific
from .models import CourseSerializer, CoreRequirementSerializer, IncludesSerializer, DegreespecificRequirementSerializer, IncludesDegreespecificSerializer,DegreeProgramSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status



def create_degree_program(request):
    if request.method == 'POST':
        form = DegreeProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('degree_program_list')
    else:
        form = DegreeProgramForm()

    return render(request, 'create_degree_program.html', {'form': form})

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()

    return render(request, 'create_course.html', {'form': form})

def degree_program_list(request):
    degree_programs = DegreeProgram.objects.all()
    return render(request, 'degree_program_list.html', {'degree_programs': degree_programs})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})



def model_list(request):
    # Determine the model type based on the URL
    model_type = request.path.split('/')[-2]  # Extract the second-to-last part of the URL
    
    # Get the 'sort' parameter from the URL
    sort_param = request.GET.get('sort', 'name')  # Default sorting by 'name'

    # Use the model type to fetch the corresponding queryset
    if model_type == 'degree_program_list':
        objects = DegreeProgram.objects.all()

        # Handle numeric sorting separately
        if sort_param in ['TotalCredits']:
            objects = sorted(objects, key=lambda x: int(getattr(x, sort_param)))
        else:
            objects = objects.order_by(sort_param)

    elif model_type == 'course_list':
        objects = Course.objects.all().order_by(sort_param)
    else:
        # Handle other model types or provide a default queryset
        objects = []

    print("Sorted Objects:", objects)

    return render(request, 'model_list.html', {'degree_programs': objects, 'sort_param': sort_param, 'model_type': model_type})

def student_detail(request, student_id):
    student = Student.objects.get(pk=student_id)
    enrollments = EnrollsIn.objects.filter(student=student).select_related('degree_program__Department')
    
    return render(request, 'student_detail.html', {
        'student': student,
        'enrollments': enrollments,
    })

def degree_detail(request, program_id):
    degree = get_object_or_404(DegreeProgram, pk=program_id)
    core_requirements = Includes.objects.filter(course__degree_program=degree).select_related('core_requirement')
    courses = Includes.objects.filter(course__degree_program=degree).select_related('course')

    degreespecific_requirements = IncludesDegreespecific.objects.filter(course__degree_program=degree).select_related('degreespecific_requirement')
    degreespecific_courses = IncludesDegreespecific.objects.filter(course__degree_program=degree).select_related('course')
    return render(request, 'degree_detail.html', {
        'degree': degree,
        'core_requirements': core_requirements,
        'courses': courses,
        'degreespecific_requirements': degreespecific_requirements,
        'degreespecific_courses': degreespecific_courses,
    })

@api_view(['GET'])
def api_degree_detail(request, program_id):
    degree = get_object_or_404(DegreeProgram, pk=program_id)
    
    core_requirements = Includes.objects.filter(course__degree_program=degree).select_related('core_requirement')
    degreespecific_requirements = IncludesDegreespecific.objects.filter(course__degree_program=degree).select_related('degreespecific_requirement')

    core_requirements_serialized = IncludesSerializer(core_requirements, many=True).data
    degreespecific_requirements_serialized = IncludesDegreespecificSerializer(degreespecific_requirements, many=True).data

    return Response({
        'degree': {
            'id': degree.id,
            'ProgramName': degree.ProgramName,
            'Department': degree.Department.DepartmentName,
        },
        'core_requirements': core_requirements_serialized,
        'degreespecific_requirements': degreespecific_requirements_serialized,
    })

class DegreeDetailView(APIView):
    def get(self, request, program_id):
        degree = DegreeProgram.objects.get(ProgramID=program_id)
        serializer = DegreeProgramSerializer(degree)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

def admin_interface(request):
    degree_programs = DegreeProgram.objects.all()
    return render(request, 'admin_template.html', {'degree_programs': degree_programs})
