from django.db import models

from utils.models import AuthoredModel
from .comment import Comment


class Like(AuthoredModel):
    comment = models.ForeignKey(Comment)
