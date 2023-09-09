from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from backend.core.models import ClubInfo, SectionGroup, Lesson, Partner, Post, Section, Personal
from backend.core.serializers import ClubInfoSerializer, SectionGroupSerializer, LessonSerializer,\
    PartnerSerializer, PostSerializer, SectionSerializer, PersonalSerializer


class ClubInfoViewSet(mixins.ListModelMixin):
    serializer_class = ClubInfoSerializer
    queryset = ClubInfo.objects.all()


class SectionGroupViewSet(mixins.ListModelMixin):
    serializer_class = SectionGroupSerializer
    queryset = SectionGroup.objects.all()


class LessonViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    def get_queryset(self):
        return super().get_queryset().select_related('group')


class PartnerViewSet(mixins.ListModelMixin):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()


class PostViewSet(mixins.ListModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class SectionViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()

    def get_queryset(self):
        return super().get_queryset().prefetch_related('trainers', 'groups')


class PersonalViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = PersonalSerializer
    queryset = Personal.objects.all()

    def get_queryset(self):
        return super().get_queryset().select_related('Section')

