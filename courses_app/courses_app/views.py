from django.shortcuts import render, redirect
from django.views import View
from .models import Courses
from .utils import create_course_form
from django.http import HttpResponse


class CoursesPage(View):
    def get(self, request):
        return render(request, 'courses_page.html')


class CoursesAddPage(View):
    def get(self, request):
        courses = Courses.objects.all()
        return render(request, 'courses_add_page.html' , {'courses': courses})

    def post(self, request):
        # form = create_course_form(request.POST)
        # if form.is_valid():
            # request.session['add-course'] = form.cleaned_data
            course_name = request.POST.get('course_name')

            # course_name = form.cleaned_data.get('course_name')
            courses = Courses(name=course_name)
            courses.save()
            return redirect('add-course')

            # return HttpResponse("Data successfully inserted!")

