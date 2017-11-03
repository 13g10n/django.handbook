from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from .views import TestView

from manuals.views import ManualViewSet
from accounts.views import UserViewSet


urlpatterns = [
    url(r'^$', TestView.as_view()),

    url(r'^admin/', admin.site.urls),
    url(r'^api/accounts/', include('authentication.urls')),
]

router = DefaultRouter()
router.register(r'api/manuals', ManualViewSet, base_name='manuals')
router.register(r'api/users', UserViewSet, base_name='users')


urlpatterns += router.urls
