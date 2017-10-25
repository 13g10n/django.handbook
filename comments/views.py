from .models import Comment
from rest_framework.viewsets import ModelViewSet
from .serializers import CommentSerializer


class CommentViewSet(ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
