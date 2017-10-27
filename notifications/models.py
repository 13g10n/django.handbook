from django.contrib.auth import get_user_model
from django.db import models


class Notification(models.Model):
    user = models.ForeignKey(get_user_model())
    title = models.CharField(max_length=64)
    text = models.CharField(max_length=140)
