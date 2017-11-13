from rest_framework.serializers import ModelSerializer, SlugRelatedField, SerializerMethodField

from manuals.models import Topic
from manuals.serializers.comment import CommentSerializer
from ..models import Manual

from accounts.serializers import AccountSerializer
from .rating import RatingSerializer
from .topic import TopicSerializer
from .step import StepSerializer


class ManualListSerializer(ModelSerializer):
    topic = TopicSerializer()
    author = AccountSerializer(read_only=True)
    rating = RatingSerializer()

    class Meta:
        model = Manual
        fields = ('id', 'title', 'created', 'topic', 'content', 'author', 'rating')


class ManualDetailSerializer(ModelSerializer):
    topic = TopicSerializer()
    author = AccountSerializer(read_only=True)
    rating = RatingSerializer(read_only=True)
    steps = StepSerializer(many=True, required=False)
    tags = SlugRelatedField(many=True, read_only=True, slug_field='word', required=False)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Manual
        fields = ('id', 'title', 'created', 'topic',
                  'rating', 'author', 'tags', 'steps', 'content', 'cover', 'comments')

    def create(self, validated_data):
        # dirty!
        topic = Topic.objects.get(title=validated_data.pop('topic')['title'])
        manual = Manual.objects.create(topic=topic, **validated_data)
        manual.save()
