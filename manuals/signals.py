from channels import Group
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from rest_framework.renderers import JSONRenderer

from manuals.models import Comment
from manuals.serializers.comment import CommentSerializer
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


@receiver(post_save, sender=Comment)
def create_comment(sender, instance, created, **kwargs):
    if created:
        serialized = CommentSerializer(instance)
        Group("post-{0}".format(instance.pk)).send({
            "text": JSONRenderer().render(serialized.data)
        })
