from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..models import ClubInfo, SectionGroup, Lesson, Partner, Post, Section, Personal
from ..serializers import ClubInfoSerializer, SectionGroupSerializer, LessonSerializer,\
    PartnerSerializer, PostSerializer, SectionSerializer, PersonalSerializer


class BaseCommonModelViewSet(mixins.ListModelMixin, GenericViewSet, mixins.RetrieveModelMixin):
    """
    A viewset that provides default `list()`action.
    """
    pass


class ClubInfoViewSet(BaseCommonModelViewSet):
    serializer_class = ClubInfoSerializer
    queryset = ClubInfo.objects.all()


class SectionGroupViewSet(BaseCommonModelViewSet):
    serializer_class = SectionGroupSerializer
    queryset = SectionGroup.objects.all()

    def get_queryset(self):
        return super().get_queryset().prefetch_related('section')


class LessonViewSet(BaseCommonModelViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    def get_queryset(self):
        return super().get_queryset().select_related('group')


class PartnerViewSet(BaseCommonModelViewSet):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()


class PostViewSet(BaseCommonModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class SectionViewSet(BaseCommonModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()

    def get_queryset(self):
        return super().get_queryset().prefetch_related('personal')


class PersonalViewSet(BaseCommonModelViewSet):
    serializer_class = PersonalSerializer
    queryset = Personal.objects.all()

    def get_queryset(self):
        return super().get_queryset().prefetch_related('section', 'job')

