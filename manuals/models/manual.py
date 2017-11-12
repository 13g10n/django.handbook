from django.db import models

from utils.models import PostModel
from .tag import Tag
from .topic import Topic


class Manual(PostModel):
    class Meta:
        ordering = ['-created']

    topic = models.ForeignKey(Topic)
    title = models.CharField(max_length=140)
    tags = models.ManyToManyField(Tag)
    cover = models.URLField(default="https://semantic-ui.com/images/wireframe/image.png")

    def __str__(self):
        return "{0} by {1} {2}".format(self.title, self.author.first_name, self.author.last_name)
