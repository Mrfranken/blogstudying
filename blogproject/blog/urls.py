from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^post/(?P<pk>\d+)$', views.detail, name='detail'),
    url(r'^archives/(?P<year>\d+)/(?P<month>\d+)$', views.archives, name='archives'),
    url(r'^category/(?P<category_id>\d+)$', views.category, name='category'),
]
