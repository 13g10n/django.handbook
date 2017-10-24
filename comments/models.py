from django.contrib.auth import get_user_model
from django.db import models

from manuals.models import Manual


class Comment(models.Model):

    class Meta:
        ordering = ["-date"]

    user = models.ForeignKey(get_user_model())
    manual = models.ForeignKey(Manual)

    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()