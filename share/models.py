from django.db import models
from user.models import User
import uuid
# Create your models here.

TYPE = (
    ('Post','POST'),
    ('Story','STORY'),
    ('Reels','REELS'),
)

class Share(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(choices=TYPE, max_length=50)
    type_id = models.UUIDField()
    user = models.ManyToManyField(User, related_name='users')
    share = models.ManyToManyField(User, related_name='shares')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)


    def created_by(self):
        return ", ".join([str(i) for i in self.user.all()])

    def share_to(self):
        return ", ".join([str(i) for i in self.share.all()])