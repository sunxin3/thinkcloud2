from django.conf.urls.defaults import patterns, url

from .views import IndexView, CreateView, UpdateView, DetailView


urlpatterns = patterns('openstack_dashboard.dashboards.project.physical_servers.views',
    url(r'^physical_servers/$', IndexView.as_view(), name='index'),
    url(r'^create/$', CreateView.as_view(), name='create'),
    url(r'^(?P<server_id>[^/]+)/update/$', UpdateView.as_view(), name='update'),
    url(r'^(?P<server_id>[^/]+)/detail/$', DetailView.as_view(), name='detail'),
    url(r'^(?P<server_id>[^/]+)/detail/$', DetailView.as_view(), name='detail'),
)
