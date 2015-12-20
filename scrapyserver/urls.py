from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
                       url(r'^accounts/login/$', auth_views.login, name="login"),
                       url(r"^$", login_required(TemplateView.as_view(
                           template_name="index.html"))),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^tutorial/', include("tutorial.urls"))
                       )
