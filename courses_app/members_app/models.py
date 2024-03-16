from django.db import models
from django.contrib.auth.models import User
from courses_app.models import Courses
from datetime import datetime


class UserEnrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.user)
