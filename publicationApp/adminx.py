from django.contrib import admin

# Register your models here.

import xadmin
from publicationApp.models import Publication


class PublicationAdmin(object):
    """xadmin后台注册"""
    list_display = ['id', 'journal', 'year', 'title', 'author', 'link', 'photo']
    fields = ['journal', 'year', 'title', 'author', 'link', 'photo']


xadmin.site.register(Publication, PublicationAdmin)
