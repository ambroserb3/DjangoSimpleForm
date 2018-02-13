from django.conf.urls import url
from . import views
from django.utils import timezone
from posts.models import User


urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^login', views.login), #login a user
  url(r'^logout', views.logout), # logout a user
  #url(r'^dashboard$', views.get_dashboard_data), # fetch dashboard data and load dashboard
  # url(r'^$', include('posts.urls')),
  # url(r'^posts/', include('posts.urls')),
];