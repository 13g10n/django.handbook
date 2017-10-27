from rest_framework.serializers import ModelSerializer, SlugRelatedField

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
    tags = SlugRelatedField(many=True, read_only=True, slug_field='word')

    class Meta:
        model = Manual
        fields = ('id', 'title', 'created', 'topic', 'rating', 'author', 'tags', 'steps', 'content')
