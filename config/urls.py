from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/accounts/', include('authentication.urls')),
]

from manuals.views import ManualViewSet
from comments.views import CommentViewSet

router = DefaultRouter()
router.register(r'api/manuals', ManualViewSet, base_name='manuals')
router.register(r'api/comments', CommentViewSet, base_name='comments')


urlpatterns += router.urls
