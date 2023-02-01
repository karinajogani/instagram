from django.db import models
from user.models import User
from django.conf import settings
import uuid
# Create your models here.
class Reels(models.Model):
    reels_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video = models.FileField(upload_to='reels_video/')
    caption = models.CharField(max_length=255)
    user = models.ManyToManyField(User, related_name='%(class)s_created_by')
    views = models.ManyToManyField(User, related_name='%(class)s_viewed_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


    def created_by(self):
        return ", ".join([str(i) for i in self.user.all()])

    def viewed_by(self):
        return ", ".join([str(i) for i in self.views.all()])

