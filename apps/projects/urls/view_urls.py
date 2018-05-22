# ~*~ coding: utf-8 ~*~
from __future__ import unicode_literals


from django.conf.urls import url
from .. import views

__all__ = ["urlpatterns"]

app_name = "projects"

urlpatterns = [
    # TResource projects url
    url(r'^project$', views.ProjectsListView.as_view(), name='projects-list'),
    url(r'^project/create/$', views.ProjectsCreateView.as_view(), name='projects-create'),
    url(r'^project/(?P<pk>[0-9a-zA-Z\-]{36})/update$', views.ProjectsUpdateView.as_view(), name='projects-update'),
    url(r'^project/(?P<pk>[0-9a-zA-Z\-]{36})$', views.ProjectsDetailView.as_view(), name='projects-detail'),
    url(r'^publish$', views.ProjectsPublishListView.as_view(), name='projects-publish'),
    url(r'^publish/publish-log/$', views.ProjectsPublishPushView.as_view(), name='projects-log'),
]