from django.contrib import admin

import xadmin
from newsApp.models import News

# Register your models here.


class NewsAdmin(object):
    """xadmin后台注册"""
    list_display = ['id', 'photo', 'title', 'text', 'time']
    fields = ['photo', 'title', 'text', 'time']


xadmin.site.register(News, NewsAdmin)

