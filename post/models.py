from django.db import models
from user.models import User
from django.conf import settings
import uuid

# Create your models here.

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    photo = models.ImageField(upload_to='postapi/')
    caption = models.TextField(blank=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name="created_by")
    # updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


    # def created_by(self):
    #     return ", ".join([str(i) for i in self.user.all()])