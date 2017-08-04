from django.conf.urls import url

from . import views

app_name = 'gist'
urlpatterns = [
    url(r'^all$', views.all, name='all'), # ex: /gist/all
    url(r'^$', views.new_gist, name='new_gist'), # ex: /gist/
    url(r'^(?P<gist_id>[0-9]+)/$', views.detail, name='detail'), # ex: /gist/5/
]
