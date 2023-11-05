from rest_framework import serializers
from .models import ClubInfo, Personal, Section, Post, Partner, Lesson, SectionGroup, PeriodicLesson


class ClubInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubInfo
        fields = '__all__'


class SectionGroupSerializer(serializers.ModelSerializer):
    section = serializers.StringRelatedField(many=True)

    class Meta:
        model = SectionGroup
        fields = ('id', 'title', 'section')


class LessonSerializer(serializers.ModelSerializer):
    group = serializers.StringRelatedField(many=False)
    section = serializers.StringRelatedField(many=False)

    class Meta:
        model = Lesson
        fields = ('group', 'section', 'date', 'start_time', 'end_time', 'periodic_id')


class PeriodicLessonSerializer(serializers.ModelSerializer):
    group = serializers.StringRelatedField(many=False)
    section = serializers.StringRelatedField(many=False)

    class Meta:
        model = PeriodicLesson
        fields = ('group', 'section', 'day', 'start_time', 'end_time', 'start_date', 'end_date')


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
    personal = serializers.StringRelatedField(many=True)

    class Meta:
        model = Section
        fields = ('id', 'name', 'description', 'image', 'is_free', 'cost', 'is_active', 'personal')


class PersonalSerializer(serializers.ModelSerializer):
    job = serializers.StringRelatedField(many=True)
    section = serializers.StringRelatedField(many=True)

    class Meta:
        model = Personal
        fields = ('id', 'section', 'fio', 'vk_id', 'tg_id', 'description', 'image', 'phone', 'job')
