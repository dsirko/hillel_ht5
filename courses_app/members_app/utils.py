from django.shortcuts import redirect
from .my_form import MemberForm, UserEnrollmentForm


def create_member_form(request_data=None):
    """
    Create a member form.
    Args:
        request_data (dict, optional): The data to initialize the form with. Defaults to None.
    Returns:
        MemberForm: The created member form.
    """
    if request_data:
        return MemberForm(request_data)

    return MemberForm()

def create_user_enrollment_form(request_data=None):
    """
    Create a user enrollment form.
    Args:
        request_data (dict): Optional dictionary containing the request data.
    Returns:
        UserEnrollmentForm: The user enrollment form.

    """
    if request_data:
        return UserEnrollmentForm(request_data)

    return UserEnrollmentForm()


def session_delete(request):
    """
    A function to delete a session if the request method is 'POST'.
    Parameters:
        request (HttpRequest): The request object containing session information.
    Returns:
        None
    """
    if request.method == 'POST':
        del request.session['session']
        redirect('sessions-view')

