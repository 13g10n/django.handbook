import json
from channels import Group

from .models import Notification
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Notification)
def notification_created(sender, instance, created, **kwargs):
    if created:
        Group("notification-{0}".format(instance.user.pk)).send({
            "text": json.dumps({
                "title": instance.title,
                "text": instance.text
            })
        })
