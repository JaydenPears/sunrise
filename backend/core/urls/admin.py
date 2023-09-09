from django.urls import include, path
from rest_framework.routers import DefaultRouter

from ..views import ClubInfoAdminViewSet, SectionGroupAdminViewSet, LessonAdminViewSet, PartnerAdminViewSet, \
    PersonalAdminViewSet, PostAdminViewSet, SectionAdminViewSet

router = DefaultRouter()
router.register(r'clubinfo', ClubInfoAdminViewSet, basename='admin-clubinfo')
router.register(r'groups', SectionGroupAdminViewSet, basename='admin-groups')
router.register(r'lessons', LessonAdminViewSet, basename='admin-lessons')
router.register(r'partners', PartnerAdminViewSet, basename='admin-partners')
router.register(r'personal', PersonalAdminViewSet, basename='admin-personal')
router.register(r'posts', PostAdminViewSet, basename='admin-posts')
router.register(r'section', SectionAdminViewSet, basename='admin-sections')


urlpatterns = [
    path('', include(router.urls)),
]
