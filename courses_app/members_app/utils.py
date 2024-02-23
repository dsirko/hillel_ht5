from django.shortcuts import redirect
from .my_form import MemberForm


def create_member_form(request_data=None):
    if request_data:
        return MemberForm(request_data)

    return MemberForm()


def process_request_session_member(request):
    if request.method == 'POST':
        form = create_member_form(request_data=request.POST)
        if form.is_valid():
            redirect('member_input')


def session_delete(request):
    if request.method == 'POST':
        del request.session['session']
        redirect('sessions-view')

