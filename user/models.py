from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid

# Create your models here.

GENDER = (
    ('Male','MALE'),
    ('Female','FEMALE'),
    ('Other','OTHER'),
)

ACCOUNTTYPE = (
    ('Public', 'PUBLIC'),
    ('Private', 'PRIVATE'),
)

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER, max_length=55)
    email_id = models.EmailField(max_length=500)
    password = models.CharField(max_length=30)
    account_type = models.CharField(choices=ACCOUNTTYPE, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance= True, created= False, **kwargs):

    if created:
        Token.objects.create(user= instance)