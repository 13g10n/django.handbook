from channels import Group
from channels.generic.websockets import WebsocketConsumer
from channels.handler import AsgiRequest
from rest_framework.authtoken.models import Token


class NotificationConsumer(WebsocketConsumer):
    http_user = True

    def connection_groups(self, **kwargs):
        return ["test"]

    def connect(self, message, **kwargs):
        request = AsgiRequest(message)
        token = request.GET.get("token", None)
        user = Token.objects.get(key=token).user
        if user:
            Group("notification-{0}".format(user.pk)).add(message.reply_channel)
            self.message.reply_channel.send({"accept": True})

    def receive(self, text=None, bytes=None, **kwargs):
        pass

    def disconnect(self, message, **kwargs):
        Group("notification").discard(message.reply_channel)