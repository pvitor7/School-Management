import uuid
from django.db import models

# Create your models here.
class Campus(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(null=False, blank=False, max_length=48)
    adress = models.CharField(null=False, blank=False, max_length=48)
    created_at = models.DateTimeField(auto_now_add=True)
    
    