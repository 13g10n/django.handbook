from django.db import models

from utils.models import AuthoredModel
from .manual import Manual


class Rating(models.Model):
    manual = models.OneToOneField(Manual, on_delete=models.CASCADE)

    votes = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)

    @property
    def average(self):
        if self.votes == 0:
            return 0
        return self.total / self.votes

    def __str__(self):
        return "Rating object for '{0}'".format(self.manual.title)


class UserRate(AuthoredModel):
    rating = models.ForeignKey(Rating)
    score = models.PositiveIntegerField()

    def __init__(self, *args, **kwargs):
        super(UserRate, self).__init__(*args, **kwargs)
        self.old_score = self.score

    def save(self, *args, **kwargs):
        if self.score < 0:
            self.score = 0
        elif self.score > 5:
            self.score = 5
        super(UserRate, self).save(*args, **kwargs)

    def __str__(self):
        return "{0} {1} voted {2} on '{3}'".format(
            self.author.first_name, self.author.last_name,
            self.score, self.rating.manual.title)
