from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'liberator.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^manager/$', 'article_manager.views.articles_list', name="article_list"),
    url(r"^manager/articles/(?P<article_id>\d+)$", "article_manager.views.article_view", name="article_view"),
    url(r"^manager/import/(?P<wiki_slug>[^/]+)/(?P<script>lat|cyr)", "article_manager.views.wiki_import", name="wiki_import"),
    url(r"^manager/extend/(?P<wiki_slug>[^/]+)/(?P<article_id>\d+|auto)/(?P<script>lat|cyr)", "article_manager.views.wiki_extend", name="wiki_extend"),
    url(r"manager/articles/(?P<article_id>\d+)/delete", "article_manager.views.article_delete", name="article_delete"),
    url(r"^manager/articles/(?P<article_id>\d+)/diff", "article_manager.views.article_diff", name="article_diff"),
    url(r"^manager/approve/(?P<article_id>\d+)", "article_manager.views.article_approve", name="article_approve"), 
    url(r"^editor/new", "article_editor.views.article_submit", name="article_submit"),
    url(r"^editor/(?P<article_id>\d+)/(?P<script>lat|cyr)", "article_editor.views.article_submit", name="article_submit"),
    url(r"^login", "author_manager.views.author_login", name="author_login"),
    url(r"^logout", "author_manager.views.author_logout", name="author_logout"),
    url(r'^admin/', include(admin.site.urls)),
)
