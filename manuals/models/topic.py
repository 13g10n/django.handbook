from django.db import models

COLORS = (
    ("red", "Red"),
    ("blue", "Blue"),
    ("green", "Green")
)


class Topic(models.Model):
    title = models.CharField(max_length=20)
    color = models.CharField(max_length=10, choices=COLORS, default="blue")

    def __str__(self):
        return self.title
