from django.urls import re_path
from django.contrib.sitemaps.views import sitemap  # Import the sitemap view function

from blog.sitemaps import BlogSitemap
from blog.views import BlogDetailView, BlogIndexView, \
                        BlogPostsRssFeed, BlogPostsAtomFeed

urlpatterns = [
    # blog urls
    re_path(r'^$', BlogIndexView.as_view(), name="blog"),
    re_path(r'^(?P<slug>[-\w]+)/$', BlogDetailView.as_view(), name="blog_detail"),

    # rss & atom feed
    re_path(r'^feed/rss$', BlogPostsRssFeed(), name="blog_rss_feed"),
    re_path(r'^feed/atom', BlogPostsAtomFeed(), name="blog_atom_feed"),

    # sitemap
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': {'blog': BlogSitemap()}}, name="blog_sitemap"),
]
