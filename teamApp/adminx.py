from django.contrib import admin

# Register your models here.


import xadmin
from teamApp.models import Team


class TeamAdmin(object):
    """xadmin后台注册"""
    list_display = ['id', 'name', 'position', 'positionType', 'background', 'bio', 'email',
                    'detail', 'researchInterest', 'interest', 'photo']
    fields = ['name', 'position', 'positionType', 'background', 'bio', 'email', 'detail', 'researchInterest', 'interest', 'photo']


xadmin.site.register(Team, TeamAdmin)