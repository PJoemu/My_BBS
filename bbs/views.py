# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework import generics
from rest_framework.parsers import JSONParser
import models
import serializers
from serializers import BbsPostSerializer
from serializers import JSONResponse


# Create your views here.
def index(request):
    bbs_objs = models.BbsPost.objects.all()
    return render_to_response('index.html', {'bbs_list': bbs_objs})


def bbs_detail(request, bbs_id):
    bbs_obj = models.BbsPost.objects.get(id=bbs_id)
    return render_to_response('bbs_detal.html', {'bbs': bbs_obj})


@csrf_exempt
def bbs_detail_rest(request, pk):
    """
    查找,更新或删除一个models.BbsPost.
    """
    try:
        obj = models.BbsPost.objects.get(pk=pk)
    except models.BbsPost.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BbsPostSerializer(obj)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BbsPostSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, stats=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)


def bbs_all(request):
    """
    查询所有
    """
    objs = models.BbsPost.objects.all()
    serializer = BbsPostSerializer(objs)
    return JSONResponse(serializer.data)


class BbsUserView(generics.ListCreateAPIView):
    model = models.BbsUser
    serializer_class = serializers.BbsUserSerializer

    permission_classes = [
        permissions.AllowAny,
    ]


class BbsUserDetailView(generics.ListAPIView):
    model = models.BbsUser
    serializer_class = serializers.BbsUserSerializer

    def get_queryset(self):
        queryset = super(BbsUserDetailView, self).get_queryset()
        return queryset.filter(user__id=self.kwargs.get('id'))
