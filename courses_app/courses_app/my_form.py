from django import forms


class NewCourseForm(forms.Form):
    name = forms.CharField(max_length=255)
