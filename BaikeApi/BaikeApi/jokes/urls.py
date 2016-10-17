from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from jokes import views

urlpatterns = [
    url(r'^jokes/$', views.JokeList.as_view()),
    url(r'^jokes/(?P<id>[0-9]+)/$', views.JokeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)