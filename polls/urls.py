from django.conf.urls import patterns, include, url


urlpatterns = patterns('polls.views',
    url(r'^$', 'view_index', name='home'),
)
