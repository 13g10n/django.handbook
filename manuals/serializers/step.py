from rest_framework.serializers import ModelSerializer, SlugRelatedField

from ..models import Step


class StepSerializer(ModelSerializer):
    attachments = SlugRelatedField(many=True, read_only=True, slug_field='url')

    class Meta:
        model = Step
        fields = ('order', 'title', 'content', 'attachments')
