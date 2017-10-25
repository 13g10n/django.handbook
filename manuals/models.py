from django.contrib.auth import get_user_model
from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Tag(models.Model):
    word = models.CharField(max_length=20)

    def __str__(self):
        return self.word


class Manual(models.Model):

    class Meta:
        ordering = ["-created", ]

    title = models.CharField(max_length=140)
    meta = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), related_name="manuals")

    topic = models.ForeignKey(Topic)
    tags = models.ManyToManyField(Tag, related_name="manuals")

    # TODO: Add cover image

    def __str__(self):
        return self.title


class Step(models.Model):
    manual = models.ForeignKey(Manual, related_name='steps')
    title = models.CharField(max_length=140)
    body = models.TextField()
    index = models.PositiveSmallIntegerField()

    # TODO: Add images [1..3]