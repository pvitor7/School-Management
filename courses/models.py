import uuid
from django.db import models
from campus.models import Campus

class Courses(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(null=False, blank=False, max_length=48)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    