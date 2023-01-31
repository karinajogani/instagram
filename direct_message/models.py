from django.db import models
from user.models import User
from django.conf import settings
import uuid
# Create your models here.

class DirectMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message = models.TextField()
    user = models.ManyToManyField(User, related_name='%(class)s_created_by')
    # updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='updated_by', blank=True, null=True)
    send = models.ManyToManyField(User, related_name='%(class)s_send_to')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=True)

    def created_by(self):
        return ", ".join([str(i) for i  in self.user.all()])

    def send_to(self):
        return ", ".join([str(i) for i in self.send.all()])