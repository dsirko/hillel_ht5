from django.contrib import admin

from .models import UserEnrollment
from courses_app.models import Courses

admin.site.register(Courses)
admin.site.register(UserEnrollment)

# Register your models here.
