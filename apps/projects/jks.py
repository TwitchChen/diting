#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jenkins
"""
@author: ChenHao
@file: jenkins
@time: 2018.5.3 15:34
"""

jenkins_server_url = "http://127.0.0.1:8080"
user_name = "developer"
user_pass = "pwd123"
api_token = "6dfc3a561e56cf29cd3eb522ae391618"


server = jenkins.Jenkins(jenkins_server_url, username=user_name, password=user_pass)
# param_dict = {"RUN_ENV":"test", "POD_NUM":"1"}
# build = server.build_job("html-fbdsc-admin-web", parameters=param_dict)
# print(build)

class ProjectsPublishPush():
    def text_log(self):
        text = "aaaaa"