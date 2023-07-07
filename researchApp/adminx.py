from django.contrib import admin

# Register your models here.


import xadmin
from researchApp.models import Research


class ResearchAdmin(object):
    """xadmin后台注册"""
    list_display = ['id', 'title', 'detail']
    fields = ['title', 'detail']


xadmin.site.register(Research, ResearchAdmin)
