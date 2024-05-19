from django.urls import include, re_path
from django.contrib import admin
from django.contrib.sitemaps import views as sitemaps_views
from django.views.decorators.cache import cache_page

from blog.sitemaps import BlogSitemap
from nouns.views import ChannelDetail
from profiles.sitemaps import ProfileSitemap
from premises.sitemaps import ArgumentSitemap, PremiseSitemap

admin.autodiscover()

sitemaps = {
    'blog': BlogSitemap(),
    'user': ProfileSitemap(),
    'argument': ArgumentSitemap(),
    'premise': PremiseSitemap()
}

urlpatterns = [
    re_path(r'^', include('newsfeed.urls')),
    re_path(r'^', include('premises.urls')),
    re_path(r'^', include('profiles.urls')),
    re_path(r'^blog/', include('blog.urls')),
    re_path(r'^nouns/', include('nouns.urls')),
    re_path(r'^channels/(?P<slug>[-\w]+)$',
        ChannelDetail.as_view(), name="channel_detail"),
    re_path(r'^', include('social_auth.urls')),
    re_path(r'^admin/', include(admin.site.urls)),
    re_path(r'^api/', include('api.urls')),

    # Sitemap
    re_path(r'^sitemap\.xml$',
        cache_page(86400)(sitemaps_views.index),
        {'sitemaps': sitemaps, 'sitemap_url_name': 'sitemaps'}),
    re_path(r'^sitemap-(?P<section>.+)\.xml$',
        cache_page(86400)(sitemaps_views.sitemap),
        {'sitemaps': sitemaps}, name='sitemaps'),
]
