from django.db import models

from utils.models import PostModel
from .manual import Manual


class Comment(PostModel):
    manual = models.ForeignKey(Manual)
