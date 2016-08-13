# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import models


class JSONResponse(HttpResponse):
    """
    一个HttpResponse,将content渲染为JSON
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class BbsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BbsPost
        # fields = ('author', 'title', 'view_count', 'ranking', 'create_time', 'modify_time')


class BbsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BbsUser
