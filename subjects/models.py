import uuid
from django.db import models
from courses.models import Courses
from users.models import User

class Subjects(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(null=False, blank=False, max_length=48)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=False)
   

class SubjectsStudants(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_1 = models.DecimalField(max_digits=3, decimal_places=1, null=True, default=None)
    test_2 = models.DecimalField(max_digits=3, decimal_places=1, null=True, default=None)
    test_3 = models.DecimalField(max_digits=3, decimal_places=1,  null=True, default=None)
    test_4 = models.DecimalField(max_digits=3, decimal_places=1,  null=True, default=None)
    