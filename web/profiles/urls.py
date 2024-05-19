from django.urls import re_path
from django.views.generic import TemplateView
from django.contrib.auth import views

from profiles.views import (RegistrationView, LoginView, LogoutView,
                            ProfileDetailView, ProfileUpdateView, ProfileChannelsGraphView, ProfileArgumentsView,
                            ProfilePremisesView, ProfileFallaciesView)


urlpatterns = [
    re_path(r'^login/$', LoginView.as_view(template_name="auth/login.html"), name='auth_login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='auth_logout'),
    re_path(r'^auth/profile$', ProfileUpdateView.as_view(
        template_name="auth/update.html"), name='auth_profile_update'),
    re_path(r'^register/$', RegistrationView.as_view(
        template_name="auth/register.html"), name='auth_registration'),
    re_path(r'^complete/$', TemplateView.as_view(
        template_name="auth/complete.html"), name='auth_registration_complete'),
    re_path(r'^users/(?P<username>[\w\._-]+)$', ProfileDetailView.as_view(
        template_name="auth/profile.html"), name='auth_profile'),
    re_path(r'^users/(?P<username>[\w\._-]+)/arguments$',
        ProfileArgumentsView.as_view(), name='auth_profile_arguments'),
    re_path(r'^users/(?P<username>[\w\._-]+)/premises$',
        ProfilePremisesView.as_view(), name='auth_profile_premises'),
    re_path(r'^users/(?P<username>[\w\._-]+)/fallacies$',
        ProfileFallaciesView.as_view(), name='auth_profile_fallacies'),
    re_path(r'^users/(?P<username>[\w\._-]+)/channels.json$',
        ProfileChannelsGraphView.as_view(), name='auth_profile_channels'),
    re_path(r'^password_reset/$', views.password_reset,
        {'template_name': 'auth/password_reset_form.html',
        'email_template_name': 'auth/password_reset_email.html'},
        name='password_reset'),
    re_path(r'^password_reset/done/$', views.password_reset_done,
        {'template_name': 'auth/password_reset_done.html'},
        name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm,
        {'template_name': 'auth/password_reset_confirm.html'},
        name='password_reset_confirm'),
    re_path(r'^reset/done/$', views.password_reset_complete,
        {'template_name': 'auth/password_reset_complete.html'},
        name='password_reset_complete'),
]
