from django.db import models

COLORS = (
    ("red", "Red"),
    ("orange", "Orange"),
    ("yellow", "Yellow"),
    ("olive", "Olive"),
    ("green", "Green"),
    ("teal", "Teal"),
    ("blue", "Blue"),
    ("violet", "Violet"),
    ("purple", "Purple"),
    ("pink", "Pink"),
    ("brown", "Brown"),
    ("grey", "Grey"),
    ("black", "Black"),
)


class Topic(models.Model):
    title = models.CharField(max_length=20)
    color = models.CharField(max_length=10, choices=COLORS, default="blue")

    def __str__(self):
        return self.title
