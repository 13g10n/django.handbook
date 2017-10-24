from django.views.generic import DetailView

from .models import Manual


class ManualDetailView(DetailView):
    # Debug only!
    model = Manual
    template_name = "manuals/detail.html"
    context_object_name = "manual"


# API VIEWS


from rest_framework.viewsets import ModelViewSet
from .serializers import ManualDetailSerializer, ManualListSerializer


class ManualViewSet(ModelViewSet):

    queryset = Manual.objects.all()
    serializer_class = ManualDetailSerializer

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