from django.db import models
from .manual import Manual


class Step(models.Model):
    manual = models.ForeignKey(Manual, related_name='steps')
    title = models.CharField(max_length=140)
    content = models.TextField(blank=True, null=True)
    order = models.PositiveSmallIntegerField()

    # TODO: Add images [1..3]

    def __str__(self):
        return "{0}. {1} for '{2}'".format(self.order, self.title, self.manual.title)
