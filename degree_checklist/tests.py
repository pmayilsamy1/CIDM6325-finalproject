# In a new file tests.py or within your existing models.py

from django.test import TestCase
from .models import DegreeProgram, Department, Course, EnrollsIn, CoreRequirement, Includes, Requires, Has, DegreespecificRequirement, IncludesDegreespecific,Student

class DegreeProgramTestCase(TestCase):
    def setUp(self):
        self.department = Department.objects.create(DepartmentName='Computer Science')
        self.degree_program = DegreeProgram.objects.create(ProgramName='Computer Science BS', TotalCredits=120, Department=self.department)

    def test_degree_program_creation(self):
        self.assertEqual(self.degree_program.ProgramName, 'Computer Science BS')
        self.assertEqual(self.degree_program.TotalCredits, 120)
        self.assertEqual(self.degree_program.Department, self.department)

class CourseTestCase(TestCase):
    def setUp(self):
        self.department = Department.objects.create(DepartmentName='Computer Science')
        self.degree_program = DegreeProgram.objects.create(ProgramName='Computer Science BS', TotalCredits=120, Department=self.department)
        self.course = Course.objects.create(CourseName='Introduction to Programming', Credits=3, Department=self.department, degree_program=self.degree_program)

    def test_course_creation(self):
        self.assertEqual(self.course.CourseName, 'Introduction to Programming')
        self.assertEqual(self.course.Credits, 3)
        self.assertEqual(self.course.Department, self.department)
        self.assertEqual(self.course.degree_program, self.degree_program)

class EnrollsInTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(FirstName='John', LastName='Doe')
        self.department = Department.objects.create(DepartmentName='Computer Science')
        self.degree_program = DegreeProgram.objects.create(ProgramName='Computer Science BS', TotalCredits=120, Department=self.department)
        self.enrollment = EnrollsIn.objects.create(student=self.student, degree_program=self.degree_program)

    def test_enrollment_creation(self):
        self.assertEqual(self.enrollment.student, self.student)
        self.assertEqual(self.enrollment.degree_program, self.degree_program)

# Add similar test cases for other models as needed
