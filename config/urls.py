from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from .views import TestView

from manuals.views import ManualViewSet, TopRatedManualApiView, TopicViewSet, comment, rate
from accounts.views import UserViewSet


urlpatterns = [
    url(r'^$', TestView.as_view()),

    url(r'^admin/', admin.site.urls),
    url(r'^api/accounts/', include('authentication.urls')),
    url(r'^api/manuals/top/', TopRatedManualApiView.as_view()),

    url(r'^api/rate/', rate),
    url(r'^api/comment/', comment)
]

router = DefaultRouter()
router.register(r'api/manuals', ManualViewSet, base_name='manuals')
router.register(r'api/users', UserViewSet, base_name='users')
router.register(r'api/topics', TopicViewSet, base_name='topics')


urlpatterns += router.urls
