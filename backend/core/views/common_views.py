from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from backend.core.models import ClubInfo, SectionGroup, Lesson, Management, Partner, Post, Section, Trainer
from backend.core.serializers import ClubInfoSerializer, SectionGroupSerializer, LessonSerializer, ManagementSerializer, \
    PartnerSerializer, PostSerializer, SectionSerializer, TrainerSerializer


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


class ManagementViewSet(mixins.ListModelMixin):
    serializer_class = ManagementSerializer
    queryset = Management.objects.all()


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


class TrainerViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = TrainerSerializer
    queryset = Trainer.objects.all()

    def get_queryset(self):
        return super().get_queryset().select_related('Section')

