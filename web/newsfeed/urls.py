from django.urls import re_path

from newsfeed.views import NewsfeedView, PublicNewsfeedView


urlpatterns = [
    re_path(r'^newsfeed$', NewsfeedView.as_view(),
        name='newsfeed'),
    re_path(r'^newsfeed/public$', PublicNewsfeedView.as_view(),
        name='public_newsfeed'),
]
