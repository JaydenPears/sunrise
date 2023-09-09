from django.urls import include, path
from rest_framework.routers import DefaultRouter

from ..views import SectionGroupViewSet, LessonViewSet, \
    PartnerViewSet, PersonalViewSet, PostViewSet, SectionViewSet

router = DefaultRouter()
router.register(r'groups', SectionGroupViewSet, basename='groups')
router.register(r'lessons', LessonViewSet, basename='lessons')
router.register(r'partners', PartnerViewSet, basename='partners')
router.register(r'personal', PersonalViewSet, basename='personal')
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'sections', SectionViewSet, basename='sections')


urlpatterns = [
    path('', include(router.urls)),
]
