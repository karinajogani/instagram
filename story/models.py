from django.db import models
from user.models import User
from django.conf import settings
import uuid

# Create your models here.
class Story(models.Model):
    story_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='stories/')
    title = models.CharField(max_length=255, blank=True)
    user = models.ManyToManyField(User, related_name='%(class)s_created_by')
    views = models.ManyToManyField(User, related_name='%(class)s_viewed_by')
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(blank=True)
    is_deleted = models.BooleanField(default=False)

    def created_by(self):
        return ", ".join([str(i) for i in self.user.all()])

    def viewed_by(self):
        return ", ".join([str(i) for i in self.views.all()])