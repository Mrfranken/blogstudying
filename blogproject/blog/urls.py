from django.conf.urls import url
from . import views

# app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>\d+)$', views.detail, name='detail'),
    url(r'^archives/(?P<year>\d+)/(?P<month>\d+)$', views.archives, name='archives'),
    url(r'^category/(?P<category_id>\d+)$', views.category, name='category'),
]
