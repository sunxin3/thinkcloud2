import logging

from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tables

from openstack_dashboard import api
from openstack_dashboard.dashboards.project.physical_servers import views
from .tables import AdminPhysicalserversTable
from .forms import CreatePhysicalServerForm, UpdatePhysicalServerForm


LOG = logging.getLogger(__name__)

class IndexView(tables.DataTableView):
    table_class = AdminPhysicalserversTable
    template_name = 'admin/physical_servers/index.html'

#    def has_more_data(self, table):
#        return self._more
    
    def get_data(self):
        request = self.request
        physical_servers = []
        try:
            physical_servers = api.nova.physical_server_list(request)
        except:
            exceptions.handle(request,
                              _('Unable to retrieve physical server list.'))

        return physical_servers
    

class CreateView(views.CreateView):
    template_name = 'admin/physical_servers/create.html'
    form_class = CreatePhysicalServerForm
    success_url = reverse_lazy('horizon:admin:physical_servers:index')


class UpdateView(views.UpdateView):
    template_name = 'admin/physical_servers/update.html'
    form_class = UpdatePhysicalServerForm
    success_url = reverse_lazy('horizon:admin:physical_servers:index')


class DetailView(views.DetailView):
    """ Admin placeholder for image detail view. """
    pass
