from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Manual, Step
from accounts.serializers import AccountSerializer

from comments.serializers import CommentSerializer


class StepSerializer(ModelSerializer):
    class Meta:
        model = Step
        fields = ('index', 'title', 'body')


class ManualListSerializer(ModelSerializer):
    topic = StringRelatedField()
    author = AccountSerializer()

    class Meta:
        model = Manual
        fields = ('id', 'title', 'meta', 'created', 'author', 'topic')


class ManualDetailSerializer(ModelSerializer):
    steps = StepSerializer(many=True)
    comments = CommentSerializer(many=True)
    tags = StringRelatedField(many=True)
    topic = StringRelatedField()
    author = AccountSerializer()

    class Meta:
        model = Manual
        fields = ('id', 'title', 'meta', 'created', 'updated', 'author', 'topic', 'tags', 'steps', 'comments')
