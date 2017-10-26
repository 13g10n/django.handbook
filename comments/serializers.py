from rest_framework.serializers import ModelSerializer
from .models import Comment
from accounts.serializers import AccountSerializer


class CommentSerializer(ModelSerializer):
    user = AccountSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'user', 'body', 'date', 'user')
