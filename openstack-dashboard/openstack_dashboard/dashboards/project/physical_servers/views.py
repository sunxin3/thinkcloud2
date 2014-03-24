import logging

from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tables
from horizon import tabs

from openstack_dashboard import api
from openstack_dashboard.dashboards.project \
        .images_and_snapshots.images import views
from .tables import PhysicalserversTable
from .forms import AdminCreateImageForm, AdminUpdateImageForm
from .tabs import PhysicalServerDetailTabs

LOG = logging.getLogger(__name__)

class IndexView(tables.DataTableView):
    table_class = PhysicalserversTable
    template_name = 'project/physical_servers/index.html'

#    def has_more_data(self, table):
#        return self._more  parse_date
    
    def get_data(self):
        request = self.request
        physical_servers = []
        try:
            server_query_result = api.nova.physical_server_list(request)
            for server in server_query_result:
                if server.is_public and (server.subscrib_user_id == request.user.id or server.subscription_id == None):
	            physical_servers.append(server)
            return physical_servers
        except:
            exceptions.handle(request,
                              _('Unable to retrieve physical server list.'))
    

class CreateView(views.CreateView):
    template_name = 'admin/images/create.html'
    form_class = AdminCreateImageForm
    success_url = reverse_lazy('horizon:admin:images:index')


class UpdateView(views.UpdateView):
    template_name = 'admin/images/update.html'
    form_class = AdminUpdateImageForm
    success_url = reverse_lazy('horizon:admin:images:index')



class DetailView(tabs.TabView):
    tab_group_class = PhysicalServerDetailTabs
    template_name = 'project/physical_servers/detail.html'
