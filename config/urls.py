from django.conf.urls import url, include
from django.contrib import admin

from .views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api/accounts/', include('authentication.urls')),
]

urlpatterns += [
    url(r'^(?P<path>.*)/$', index),
    url(r'^$', index),
]
