from django.contrib.auth import get_user_model
from django.db import models

from manuals.models import Manual


class Comment(models.Model):

    class Meta:
        ordering = ["-date"]

    user = models.ForeignKey(get_user_model())
    manual = models.ForeignKey(Manual, related_name="comments")

    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()


class CommentLike(models.Model):

    class Meta:
        ordering = ["-date"]

    comment = models.ForeignKey(Comment, related_name="likes")
    user = models.ForeignKey(get_user_model(), related_name="likes")
    date = models.DateTimeField(auto_now_add=True)
