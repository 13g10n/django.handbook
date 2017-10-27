from django.db import models
from authentication.models import EmailUserManager, EmailAbstractUser


class User(EmailAbstractUser):
    avatar = models.URLField(default="https://semantic-ui.com/images/wireframe/image.png")
    bio = models.TextField()

    objects = EmailUserManager()
