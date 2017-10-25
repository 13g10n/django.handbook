from django.contrib.auth import get_user_model
from django.db import models


class AbstractBadge(models.Model):

    class Meta:
        abstract = True

    user = models.ForeignKey(get_user_model(), related_name="%(app_label)s_%(class)s")
    date = models.DateTimeField(auto_now_add=True)

    title = "Abstract badge title"
    meta = "Abstract badge meta"

    def __str__(self):
        return "{0}: {1}".format(self.title, self.meta)

