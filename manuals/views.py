from rest_framework.response import Response

from manuals.models import UserRate, Comment
from .models import Manual, Topic
from rest_framework.viewsets import ModelViewSet
from .serializers import ManualDetailSerializer, ManualListSerializer
from rest_framework import filters
from rest_framework import generics
from .serializers.topic import TopicSerializer
from rest_framework.decorators import api_view


class ManualViewSet(ModelViewSet):

    queryset = Manual.objects.all()
    serializer_class = ManualDetailSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title', 'content', 'steps__content', 'steps__title']

    action_serializers = {
        'retrieve': ManualDetailSerializer,
        'list': ManualListSerializer,
        'create': ManualDetailSerializer
    }

    def get_serializer_class(self):

        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]

        return super(ManualViewSet, self).get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class TopRatedManualApiView(generics.ListAPIView):
    serializer_class = ManualDetailSerializer

    def get_queryset(self):
        # This part is very slow!
        return sorted(Manual.objects.all(), key=lambda m: -m.rating.average)[:5]


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title', ]


@api_view(['POST'])
def rate(request):
    # id and rate
    manual = Manual.objects.get(pk=request.data['id'])
    try:
        user_rate = UserRate.objects.get(author=request.user, rating=manual.rating)
        user_rate.score = request.data['rate']
        user_rate.save()
    except UserRate.DoesNotExist:
        user_rate = UserRate.objects.create(author=request.user, rating=manual.rating, score=request.data['rate'])
        user_rate.save()
    manual = Manual.objects.get(pk=request.data['id'])
    return Response({"rating": manual.rating.average})


@api_view(['POST'])
def comment(request):
    # id and rate
    manual = Manual.objects.get(pk=request.data['id'])
    user_comment = Comment.objects.create(author=request.user, content=request.data['content'], manual=manual)
    user_comment.save()
    return Response({"result": "success"})
