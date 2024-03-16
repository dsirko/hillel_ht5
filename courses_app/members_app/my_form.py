from django import forms


class UserEnrollmentForm(forms.Form):
    name = forms.CharField(label="User name:")
    course = forms.CharField(label="Course:")
    datetime = forms.DateTimeField(label="Enrollment date:")


class MemberForm(forms.Form):
    username = forms.CharField(label="Member's name:")
    email = forms.EmailField(label="Email:")
    age = forms.IntegerField(label="Age:")


class NewSession(forms.Form):
    username = forms.CharField(label="Member's name:")


