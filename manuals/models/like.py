from django.db import models

from .abstract import AuthoredModel
from .comment import Comment


class Like(AuthoredModel):
    comment = models.ForeignKey(Comment)
