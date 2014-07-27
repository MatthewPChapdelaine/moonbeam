from django.conf.urls import patterns, url


urlpatterns = patterns("entries.views",
    url("^$", "entries_list", name="entries_list"),
    url("^tags/(?P<keyword_slug>.*)/$", "entries_tag_list", name="entries_tag_list"),
    url("^(?P<entry_slug>.*)/$", "entries_redirect", name="entries_redirect"),
)