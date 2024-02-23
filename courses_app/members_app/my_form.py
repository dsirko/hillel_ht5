from django import forms


class MemberForm(forms.Form):
    username = forms.CharField(label="Member's name:")
    email = forms.EmailField(label="Email:")
    age = forms.IntegerField(label="Age:")


class NewSession(forms.Form):
    username = forms.CharField(label="Member's name:")


