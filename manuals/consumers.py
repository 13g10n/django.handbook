from channels import Group
from channels.generic.websockets import WebsocketConsumer
from channels.handler import AsgiRequest

from manuals.models import Manual


class CommentsConsumer(WebsocketConsumer):
    http_user = True

    def connection_groups(self, **kwargs):
        return []

    def connect(self, message, **kwargs):
        request = AsgiRequest(message)
        manual_id = request.GET.get("post", None)
        post = Manual.objects.get(id=manual_id)
        if post:
            print("Connected now to 'post-" + str(post.pk) + "' channel")
            Group("post-{0}".format(post.pk)).add(message.reply_channel)
            self.message.reply_channel.send({"accept": True})

    def receive(self, text=None, bytes=None, **kwargs):
        pass

    def disconnect(self, message, **kwargs):
        Group("notification").discard(message.reply_channel)
