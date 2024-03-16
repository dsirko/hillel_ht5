from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from datetime import datetime
from .utils import create_member_form
from django.views import View
from .models import UserEnrollment
from courses_app.models import Courses
from django.http import HttpResponse


class UserEnrollmentView(View):
    def get(self, request):
        """
        A function to retrieve all courses, users, and user enrollments and render them on the user enrollment page.

        Parameters:
            request: HttpRequest object

        Returns:
            HttpResponse object
        """
        courses = Courses.objects.all()
        users = User.objects.all()
        user_enrollments = UserEnrollment.objects.all()
        return render(request, 'user_enrollment_page.html', {'courses': courses, 'users': users, 'user_enrollments': user_enrollments})

    def post(self, request):
        """
        Handle POST requests, process form data, and render the user enrollment page.
        Takes a request object.
        Returns the rendered user enrollment page with updated data.
        """
        user_enrollments = UserEnrollment.objects.all()
        courses = Courses.objects.all()
        users = User.objects.all()
        message = None

        if 'save' in request.POST:
            coursename = request.POST.get('course')
            username = request.POST.get('username')
            user = User.objects.filter(username=username).first()
            course = Courses.objects.filter(name=coursename).first()
            user_enrl = UserEnrollment(user=user, course=course)
            user_enrl.save()
            message = {"message": f"{username} user successfully assigned to {coursename} course!", "color": "green"}

        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            enrollment = UserEnrollment.objects.get(id=pk)
            enrollment.delete()
            message = {"message": f"{enrollment.user} user successfully removed from {enrollment.course} course!", "color": "red"}


        return render(request, 'user_enrollment_page.html', {'courses': courses, 'users': users, 'message': message, 'user_enrollments': user_enrollments})


class MemberInputView(View):
    def get(self, request):
        """
        Get method to render the member input page with a create member form.

        :param request: The HTTP request object
        :return: The rendered member input page with the create member form
        """
        return render(request, 'member_input_page.html', {'form': create_member_form()})

    def post(self, request):
        """
        Handles the HTTP POST request for creating a new member.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The HTTP response object.
        """
        form = create_member_form(request.POST)
        if form.is_valid():
            request.session['member_input'] = form.cleaned_data
            return redirect('member_data')

        return render(request, 'member_input_page.html', {'form': form})

#
def member_data_view(request):
    """
    A view function that retrieves member input data from the session and renders a template with the data.

    Parameters:
    - request: HttpRequest object representing the request made to the server.

    Returns:
    - Rendered HttpResponse object displaying the 'member_data_page_view.html' template with member input data.
    """
    member_input = request.session.get('member_input', {})
    return render(request, 'member_data_page_view.html', {'member_input': member_input})


class SessionView(View):
    def get(self, request):
        """
        Get method to handle the request and session, and render the sessions view.

        :param request: The request object
        :return: The rendered sessions view
        """
        request.session['session'] = str(datetime.now())
        return render(request, 'sessions_view.html', {'request': request.session})



