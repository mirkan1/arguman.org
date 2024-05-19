from django.urls import re_path
from premises.views import (ContentionDetailView, HomeView,
                            ArgumentCreationView, PremiseCreationView,
                            PremiseDeleteView, ContentionJsonView,
                            PremiseEditView, ArgumentUpdateView,
                            ArgumentPublishView, ArgumentUnpublishView,
                            ArgumentDeleteView, AboutView, NewsView,
                            UpdatedArgumentsView, ReportView, RemoveReportView,
                            ControversialArgumentsView, TosView, SearchView,
                            NotificationsView, PremiseSupportView, PremiseUnsupportView,
                            StatsView, FallaciesView, FeaturedJSONView, NewsJSONView,
                            RandomArgumentView)


urlpatterns = [
   re_path(r'^$', HomeView.as_view(), name='home'),
   re_path(r'^notifications$', NotificationsView.as_view(), name='notifications'),
   re_path(r'^featured.json$', FeaturedJSONView.as_view(), name='contentions_featured_json'),
   re_path(r'^news.json$', NewsJSONView.as_view(), name='contentions_latest_json'),
   re_path(r'^news$', NewsView.as_view(),
       name='contentions_latest'),
   re_path(r'^search$', SearchView.as_view(),
       name='contentions_search'),
   re_path(r'^random$', RandomArgumentView.as_view(),
       name='contentions_random'),
   re_path(r'^updated$', UpdatedArgumentsView.as_view(),
       name='contentions_updated'),
   re_path(r'^controversial', ControversialArgumentsView.as_view(),
       name='contentions_controversial'),
   re_path(r'^stats$', StatsView.as_view(),
       name='contentions_stats'),
    re_path(r'^fallacies$', FallaciesView.as_view(),
       name='fallacies'),
   re_path(r'^about$',
       AboutView.as_view(),
       name='about'),
   re_path(r'^tos$',
       TosView.as_view(),
       name='tos'),
   re_path(r'^new-argument$',
       ArgumentCreationView.as_view(),
       name='new_argument'),
   re_path(r'^(?P<slug>[\w-]+)/edit$',
        ArgumentUpdateView.as_view(),
        name='contention_edit'),
   re_path(r'^(?P<slug>[\w-]+)\.json$',
        ContentionJsonView.as_view(),
        name='contention_detail_json'),
   re_path(r'^(?P<slug>[\w-]+)$',
        ContentionDetailView.as_view(),
        name='contention_detail'),
   re_path(r'^(?P<slug>[\w-]+)/(?P<premise_id>[\d+]+)$',
        ContentionDetailView.as_view(),
        name='premise_detail'),
   re_path(r'^(?P<slug>[\w-]+)/premises/(?P<pk>[0-9]+)/unsupport',
        PremiseUnsupportView.as_view(),
        name='unsupport_premise'),
   re_path(r'^(?P<slug>[\w-]+)/premises/(?P<pk>[0-9]+)/support',
        PremiseSupportView.as_view(),
        name='support_premise'),
   re_path(r'^(?P<slug>[\w-]+)/premises/(?P<pk>[0-9]+)/delete',
        PremiseDeleteView.as_view(),
        name='delete_premise'),
   re_path(r'^(?P<slug>[\w-]+)/premises/(?P<pk>[0-9]+)/report',
        ReportView.as_view(),
        name='report_premise'),
   re_path(r'^(?P<slug>[\w-]+)/premises/(?P<pk>[0-9]+)/unreport',
        RemoveReportView.as_view(),
        name='unreport_premise'),
   re_path(r'^(?P<slug>[\w-]+)/premises/(?P<pk>[0-9]+)/new',
        PremiseCreationView.as_view(),
        name='insert_premise'),
   re_path(r'^(?P<slug>[\w-]+)/premises/(?P<pk>[0-9]+)',
        PremiseEditView.as_view(),
        name='edit_premise'),
   re_path(r'^(?P<slug>[\w-]+)/premises/new',
        PremiseCreationView.as_view(),
        name='new_premise'),
    re_path(r'^(?P<slug>[\w-]+)/publish',
        ArgumentPublishView.as_view(),
        name='contention_publish'),
    re_path(r'^(?P<slug>[\w-]+)/unpublish',
        ArgumentUnpublishView.as_view(),
        name='contention_unpublish'),
    re_path(r'^(?P<slug>[\w-]+)/delete',
        ArgumentDeleteView.as_view(),
        name='contention_delete'),
]
