from django.db import models
from user.models import User
from django.conf import settings
import uuid

# Create your models here.

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    photo = models.ImageField(upload_to='postapi/')
    caption = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # updated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

