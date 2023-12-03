# custom_filters.py
from django import template

register = template.Library()

@register.filter
def total_credits(enrollments):
    return sum(course.Credits for enrollment in enrollments for course in enrollment.degree_program.courses.all())
