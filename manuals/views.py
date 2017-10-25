from .models import Manual
from rest_framework.viewsets import ModelViewSet
from .serializers import ManualDetailSerializer, ManualListSerializer
from rest_framework import filters


class ManualViewSet(ModelViewSet):

    queryset = Manual.objects.all()
    serializer_class = ManualDetailSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title', 'meta', 'steps__body', 'steps__title']

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