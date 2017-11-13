from manuals.consumers import CommentsConsumer
from notifications.consumers import NotificationConsumer

channel_routing = [
    NotificationConsumer.as_route(path=r"^/notification/"),
    CommentsConsumer.as_route(path=r"/comments/"),
]
