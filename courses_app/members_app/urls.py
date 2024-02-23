from django.urls import path
from .views import member_input_view, member_data_view, sessions_view, session_delete

urlpatterns = [
    path('', member_input_view, name='member_input'),
    path('member-data/', member_data_view, name='member_data'),
    path('sessions/', sessions_view, name='sessions-view'),
]