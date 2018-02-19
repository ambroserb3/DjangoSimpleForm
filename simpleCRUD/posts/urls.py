from django.conf.urls import url
from . import views
from django.utils import timezone
from posts.models import User


urlpatterns = [
  url(r'^$', views.user_login, name='login'), #login a user
  url(r'^logout', views.logout), # logout a user
  url(r'^register', views.register), # logout a user
]
