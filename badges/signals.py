from .models import FirstManualBadge
from django.db.models.signals import post_save
from django.dispatch import receiver
from manuals.models import Manual


@receiver(post_save, sender=Manual)
def manual_created(sender, instance, created, **kwargs):
    if created and instance.author.manuals.count() == 1:
        FirstManualBadge.objects.create(user=instance.author)
