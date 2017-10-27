from notifications.consumers import NotificationConsumer

channel_routing = [
    NotificationConsumer.as_route(path=r"^/notification/"),
]