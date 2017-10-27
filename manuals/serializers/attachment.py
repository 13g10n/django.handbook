from rest_framework.serializers import ModelSerializer

from ..models import StepAttachment


class StepAttachmentSerializer(ModelSerializer):

    class Meta:
        model = StepAttachment
        fields = ('url', )
