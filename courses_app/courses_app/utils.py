from django.shortcuts import redirect
from .my_form import NewCourseForm


def create_course_form(request_data=None):
    if request_data:
        return NewCourseForm(request_data)

    return NewCourseForm()