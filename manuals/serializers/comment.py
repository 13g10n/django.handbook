from rest_framework.serializers import ModelSerializer

from accounts.serializers import AccountSerializer
from manuals.models import Comment


class CommentSerializer(ModelSerializer):
    author = AccountSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'content')
