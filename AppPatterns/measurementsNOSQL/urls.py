from django.conf.urls import url, include

from .views import *
 
urlpatterns =[
    url(r'^estudiante/$', estudiante),
    url(r'^estudiante/(?P<pk>\w+)/$', estudianteDetail),
    url(r'^places/$', places),
    url(r'^places/(?P<pk>\w+)/$', placeDetail),
    url(r'^warnings/$', warnings),
    url(r'^warnings/(?P<pk>\w+)/$', warningDetail),
    url(r'^warningsFilter/$', warningsFilter),
    url(r'^average/(?P<pk>\w+)/$', average)
] 