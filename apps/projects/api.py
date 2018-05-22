#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/6 下午5:13
# @Author  : xiaomao
# @Site    : 
# @File    : api.py
# @Software: PyCharm

from .models import Projects
from . import serializers
from common.utils import get_logger
from .hands import IsSuperUser, IsSuperUserOrAppUser
from rest_framework_bulk import BulkModelViewSet
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse, HttpResponseRedirect
import requests
from .jks import Jks

class ProjectsViewSet(BulkModelViewSet):
    """
    Projects api set, for add,delete,update,list,retrieve resource
    """
    queryset = Projects.objects.all()
    serializer_class = serializers.ProjectsSerializer
    permission_classes = (IsSuperUserOrAppUser,)


class ProjectsUpdateGroupApi(generics.RetrieveUpdateAPIView):
    queryset = Projects.objects.all()
    serializer_class = serializers.ProjectsUpdateGroupSerializer
    permission_classes = (IsSuperUser,)


class ProjectsUpdateUserApi(generics.RetrieveUpdateAPIView):
    queryset = Projects.objects.all()
    serializer_class = serializers.ProjectsUpdateUserSerializer
    permission_classes = (IsSuperUser,)


@api_view(['GET', 'POST'])
def GetbuildLog(request):
    data = request.data
    snum = data['start']
    project = data['project']
    reqhead = request.META.get('X-ConsoleAnnotator')
    param = {"start": snum}
    print(param)
    a = Jks()
    b = a.GetCurrJobNum(project)
    url = "http://jenkins.fjf.com/job/" + project + "/" + str(b) + "/logText/progressiveHtml"
    req = requests.post(url, data=data, auth=('developer', 'pwd123'), headers=reqhead)
    print(req.headers['X-Text-Size'])
    response = HttpResponse(req.text)
    response['X-Text-Size'] = req.headers['X-Text-Size']
    response['X-ConsoleAnnotator'] = req.headers['X-ConsoleAnnotator']
    if 'X-More-Data' in req.headers.keys():
        response['X-More-Data'] = req.headers['X-More-Data']
    return response


@api_view(['POST'])
def ProjectPublishPush(request):
    data = request.data
    project = data['project']
    runenv = data['runenv']
    podnum = data['podnum']
    a = Jks()
    b = a.BuildJob(project, RUN_ENV=runenv, POD_NUM=podnum)
    print(b)
    url = '/projects/publish/publish-log/?project=' + project
    return HttpResponseRedirect(url)