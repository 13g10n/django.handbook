from rest_framework.serializers import ModelSerializer

from ..models import Step


class StepSerializer(ModelSerializer):

    class Meta:
        model = Step
        fields = ('order', 'title', 'content')