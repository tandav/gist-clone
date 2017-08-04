from django.conf.urls import url

from . import views

app_name = 'gist'
urlpatterns = [
    url(r'^$', views.index, name='index'), # ex: /gist/
    url(r'^(?P<gist_id>[0-9]+)/$', views.detail, name='detail'), # ex: /gist/5/
]
