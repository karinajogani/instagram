from django.db import models
from user.models import User
import uuid
# Create your models here.

class Follow(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    following_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_by = models.CharField()
    updated_by = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=True)
