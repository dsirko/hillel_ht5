from django.shortcuts import render, redirect
from datetime import datetime
from .utils import create_member_form, process_request_session_member, session_delete


def member_input_view(request):
    process_request_session_member(request=request)
    return render(request, 'member_input_page.html', {'form': create_member_form()})


def member_data_view(request):
    member_input = request.session.get('member_input', {})
    return render(request, 'member_data_page_view.html', {'member_input': member_input})


def sessions_view(request):
    """Save current datatime as session name and redirect to view"""
    request.session['session'] = str(datetime.now())
    return render(request, 'sessions_view.html', {'request': request.session})
