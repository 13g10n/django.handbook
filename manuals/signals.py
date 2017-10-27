from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Manual, Rating, UserRate


@receiver(post_save, sender=Manual)
def create_rating_object(sender, instance, created, **kwargs):
    if created:
        Rating.objects.create(manual=instance)


@receiver(pre_save, sender=UserRate)
def revert_rating(sender, instance, update_fields, **kwargs):
    if instance.pk:
        instance.rating.votes -= 1
        instance.rating.total -= instance.old_score
        instance.rating.save()


@receiver(post_save, sender=UserRate)
def add_rating(sender, instance, created, **kwargs):
    instance.rating.votes += 1
    instance.rating.total += instance.score
    instance.rating.save()
