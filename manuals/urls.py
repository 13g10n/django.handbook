from .views import ManualViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'manuals', ManualViewSet, base_name='manuals')
