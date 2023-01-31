from django.db import models
from user.models import User
from django.conf import settings
import uuid
# Create your models here.

class Follow(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    following = models.UUIDField()
    user = models.ManyToManyField(User)
    # updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    def created_by(self):
        return ", ".join([str(i) for i in self.user.all()])