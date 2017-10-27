from rest_framework.serializers import ModelSerializer

from ..models import Topic


class TopicSerializer(ModelSerializer):

    class Meta:
        model = Topic
        fields = ('title', 'color')
