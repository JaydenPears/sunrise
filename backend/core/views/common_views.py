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

    def get_queryset(self):
        group = self.request.query_params.get('group')
        section = self.request.query_params.get('section')
        if (group is not None) and (section is None):
            return Lesson.objects.filter(group__pk=group).select_related('group', 'section')
        elif (group is not None) and (section is not None):
            return Lesson.objects.filter(group__pk=group, section__pk=section).select_related('group', 'section')
        elif (section is not None) and (group is None):
            return Lesson.objects.filter(section__pk=section).select_related('group', 'section')
        else:
            return Lesson.objects.all().select_related('group', 'section')


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

