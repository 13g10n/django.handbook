from .models import User
from rest_framework.viewsets import ModelViewSet
from .serializers import AccountSerializer


class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = AccountSerializer
