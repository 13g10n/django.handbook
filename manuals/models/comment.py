from django.db import models

from .abstract import PostModel
from .manual import Manual


class Comment(PostModel):
    manual = models.ForeignKey(Manual)
