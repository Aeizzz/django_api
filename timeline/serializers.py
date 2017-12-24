# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import TimeLine

class TimeLineSerializer(serializers.Serializer):
    class Meta:
        model = TimeLine
        fields = '__all__'


class CreateOrEditTimeLineSerializer(serializers.Serializer):
    class Meta:
        model = TimeLine
        fields = ('text')

class CreateTimeLineSerializer(CreateOrEditTimeLineSerializer):
    pass