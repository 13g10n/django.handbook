from django.db import models
from authentication.models import EmailUserManager, EmailAbstractUser


class User(EmailAbstractUser):
    date_of_birth = models.DateField('Date of birth', null=True, blank=True)

    objects = EmailUserManager()
