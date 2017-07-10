from django.conf.urls import url
from django.views.static import serve
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    url(r'^js/(?P<path>.*)$', serve, { 'document_root': './template/js/' }),

    url(r'^css/(?P<path>.*)$', serve, { 'document_root': './template/css/' }),
    
    url(r'^images/(?P<path>.*)$', serve, { 'document_root': './template/images/' }),
]
