from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
        url(r'^admin/', include(admin.site.urls)),
        url(r'^$', 'blog.views.index'),
        # url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post'),
        # url(r'^list$', 'blog.views.post_list'),
        url(
            r'^blog/view/(?P<slug>[^\.]+).html',
            'blog.views.post',
            name='view_blog_post'),
        url(
            r'^blog/category/(?P<slug>[^\.]+).html',
            'blog.views.category',
            name='view_blog_category'),
)