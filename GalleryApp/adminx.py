from django.contrib import admin

import xadmin
from GalleryApp.models import GalleryLife, GalleryExperiment


# Register your models here.


class GalleryLifeAdmin(object):
    """xadmin后台注册"""
    list_display = ['id', 'photo', 'text']
    fields = ['photo', 'text']


class GalleryExperimentAdmin(object):
    """xadmin后台注册"""
    list_display = ['id', 'photo', 'text']
    fields = ['photo', 'text']


xadmin.site.register(GalleryLife, GalleryLifeAdmin)
xadmin.site.register(GalleryExperiment, GalleryExperimentAdmin)
