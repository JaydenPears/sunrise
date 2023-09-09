from rest_framework import serializers
from backend.core.models import ClubInfo, Trainer, Section, Post, Partner, Management, Lesson, SectionGroup


class ClubInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubInfo
        fields = '__all__'


class SectionGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionGroup
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class ManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('created_at',)


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'


