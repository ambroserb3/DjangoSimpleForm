from django.conf.urls import url
from . import views
from django.utils import timezone
from posts.models import User


urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^login', views.login), #login a user
  url(r'^logout', views.logout), # logout a user
];