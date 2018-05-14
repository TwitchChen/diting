# ~*~ coding: utf-8 ~*~
from __future__ import unicode_literals

from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .. import api


app_name = "api-projects"

router = DefaultRouter()
router.register(r'v1/projects', api.ProjectsViewSet, 'projects')

urlpatterns = [
        url(r'^v1/projects/(?P<pk>[0-9a-zA-Z\-]{36})/groups/$',
                api.ProjectsUpdateGroupApi.as_view(), name='projects-update-group'),
        url(r'^v1/projects/(?P<pk>[0-9a-zA-Z\-]{36})/users/$',
                api.ProjectsUpdateUserApi.as_view(), name='projects-update-user'),
        url(r'v1/projects/log/$', api.gettextlog, name='projects-publibsh-log'),
]

urlpatterns += router.urls