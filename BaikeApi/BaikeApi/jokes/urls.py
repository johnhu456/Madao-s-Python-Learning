from django.conf.urls import url
from jokes import views

urlpatterns = [
    url(r'^jokes/$', views.joke_list),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]