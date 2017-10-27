from rest_framework.serializers import ModelSerializer

from ..models import Manual

from accounts.serializers import AccountSerializer
from .rating import RatingSerializer
from .topic import TopicSerializer
from .step import StepSerializer


class ManualListSerializer(ModelSerializer):
    topic = TopicSerializer()

    class Meta:
        model = Manual
        fields = ('id', 'title', 'created', 'topic', 'content')


class ManualDetailSerializer(ModelSerializer):
    topic = TopicSerializer()
    author = AccountSerializer(read_only=True)
    rating = RatingSerializer()
    steps = StepSerializer(many=True)

    class Meta:
        model = Manual
        fields = ('id', 'title', 'created', 'topic', 'rating', 'author', 'steps', 'content')
