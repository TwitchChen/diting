#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jenkins
"""
@author: ChenHao
@file: jenkins
@time: 2018.5.3 15:34
"""

jenkins_server_url = "http://jenkins.fjf.com"
user_name = "developer"
user_pass = "pwd123"
api_token = "6dfc3a561e56cf29cd3eb522ae391618"



class Jks():
    def __init__(self):
        self.jenkins_server_url = "http://jenkins.fjf.com"
        self.user_name = "developer"
        self.api_token = "6dfc3a561e56cf29cd3eb522ae391618"
        self.server = jenkins.Jenkins(self.jenkins_server_url, username=self.user_name, password=self.api_token)

    def GetJobs(self, job_name):
        data = self.server.get_jobs()
        for i in data:
            if i['name'] == job_name:
                res = i
        return res


    def GetCurrJobNum(self, job_name):
        data = self.server.get_job_info(job_name)
        nbnum = data['nextBuildNumber']
        res = nbnum - 1
        return res


    def BuildJob(self, job_name, **kwargs):
        data = self.server.build_job(job_name, parameters=kwargs)
        return data