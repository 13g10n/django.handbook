from django.db import models

from .step import Step


class StepAttachment(models.Model):
    step = models.ForeignKey(Step, related_name="attachments")
    url = models.URLField()

    def save(self, *args, **kwargs):
        number_of_images = self.step.attachments.count()
        if number_of_images < 3:
            super(StepAttachment, self).save(*args, **kwargs)
        return False

    def __str__(self):
        return "Attachment for '{0}'".format(self.step.title)
