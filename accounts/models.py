from django.db import models
from authentication.models import EmailUserManager, EmailAbstractUser


LANG_CHOICES = (
    ('en', 'English'),
    ('ru', 'Русский'),
)


class User(EmailAbstractUser):
    avatar = models.URLField(default="https://semantic-ui.com/images/wireframe/image.png")
    language = models.CharField(max_length=2, choices=LANG_CHOICES, default=LANG_CHOICES[0])

    objects = EmailUserManager()
