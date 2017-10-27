from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from .views import TestView

urlpatterns = [
    url(r'^$', TestView.as_view()),

    url(r'^admin/', admin.site.urls),
    url(r'^api/accounts/', include('authentication.urls')),
]


from manuals.views import ManualViewSet

router = DefaultRouter()
router.register(r'api/manuals', ManualViewSet, base_name='manuals')


urlpatterns += router.urls
