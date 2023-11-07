from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import GenericViewSet
from ..models import ClubInfo, SectionGroup, Lesson, Partner, Post, Section, Personal, PeriodicLesson
from ..serializers import ClubInfoSerializer, SectionGroupSerializer, LessonSerializer, \
    PartnerSerializer, PostSerializer, SectionSerializer, PersonalSerializer, PeriodicLessonSerializer


class BaseAdminModelViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                            mixins.ListModelMixin, GenericViewSet, mixins.DestroyModelMixin):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `list()`, `delete()` actions.
    """
    pass


class ClubInfoAdminViewSet(BaseAdminModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = ClubInfoSerializer
    queryset = ClubInfo.objects.all()


class SectionGroupAdminViewSet(BaseAdminModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = SectionGroupSerializer
    queryset = SectionGroup.objects.all()

    def get_queryset(self):
        return super().get_queryset().prefetch_related('section')


class LessonAdminViewSet(BaseAdminModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    def get_queryset(self):
        return super().get_queryset().select_related('group', 'section')

class PeriodicLessonAdminViewSet(BaseAdminModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = PeriodicLessonSerializer
    queryset = PeriodicLesson.objects.all()

    def get_queryset(self):
        return super().get_queryset().select_related('group', 'section')


class PartnerAdminViewSet(BaseAdminModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()


class PostAdminViewSet(BaseAdminModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class SectionAdminViewSet(BaseAdminModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = SectionSerializer
    queryset = Section.objects.all()

    def get_queryset(self):
        return super().get_queryset().prefetch_related('personal')


class PersonalAdminViewSet(BaseAdminModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = PersonalSerializer
    queryset = Personal.objects.all()

    def get_queryset(self):
        return super().get_queryset().prefetch_related('section', 'job')

