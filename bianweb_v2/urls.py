"""bianweb_v2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from bianweb_v2.settings import MEDIA_ROOT

from contactApp.views import contact
from homeApp.views import home
from GalleryApp.views import galleryLife, galleryExperiment
from newsApp.views import news
from publicationApp.views import publication
from researchApp.views import research
from teamApp.views import team, member
import xadmin

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', home, name='home'),
    path('team/', team, name='team'),
    path('team/member', member, name='member'),
    path('contact/', contact, name='contact'),
    path('gallery/life', galleryLife, name='galleryLife'),
    path('gallery/experiment', galleryExperiment, name='galleryExperiment'),
    path('news/', news, name='news'),
    path('publication/', publication, name='publication'),
    path('research/', research, name='research'),
    re_path(r'media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT}),
]
