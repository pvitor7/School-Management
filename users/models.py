import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from campus.models import Roles
from classes.models import Classes

# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    first_name = models.CharField(null=False, blank=False, max_length=128)
    last_name = models.CharField(null=False, blank=False, max_length=128)
    email = models.EmailField(unique=True, null=False, blank=False)
    cellphone = models.CharField(max_length=12, null=False, blank=False, unique=True)
    classe = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True, related_name="classe")
    role = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True, related_name="role")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    