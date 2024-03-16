from django.urls import path
from .views import MemberInputView, member_data_view, SessionView, UserEnrollmentView

urlpatterns = [
    path('', MemberInputView.as_view(), name='member_input'),
    path('member-data/', member_data_view, name='member_data')
    path('sessions/', SessionView.as_view(), name='sessions-view'),
    path('user-enrollment/', UserEnrollmentView.as_view(), name='user_enrollment'),
]