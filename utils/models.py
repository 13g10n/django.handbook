from django.db import models
from django.contrib.auth import get_user_model


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created"]


class AuthoredModel(TimeStampedModel):
    author = models.ForeignKey(get_user_model())

    class Meta:
        abstract = True


class PostModel(AuthoredModel):
    content = models.TextField()

    class Meta:
        abstract = True
