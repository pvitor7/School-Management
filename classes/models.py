import uuid
from django.db import models
from courses.models import Courses

class Classes(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(null=False, blank=False, max_length=48)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    