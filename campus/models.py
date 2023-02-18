import uuid
from django.db import models

# Create your models here.
class RolesChoices(models.TextChoices):
    DEFAULT = 0
    STUDANT = 1
    ASSISTENT = 3
    TEACHER = 5
    ADMIN = 7
    OWNER = 9

class Campus(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(null=False, blank=False, max_length=48)
    adress = models.CharField(null=False, blank=False, max_length=48)
    created_at = models.DateTimeField(auto_now_add=True)
   

class Roles(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(null=False, blank=False, max_length=48, unique=True)
    permission = models.IntegerField(choices=RolesChoices.choices, default=RolesChoices.DEFAULT)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, null=False)
    