import logging

from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tables

from openstack_dashboard import api
from openstack_dashboard.dashboards.project \
        .images_and_snapshots.images import views
from .tables import AdminImagesTable
from .forms import AdminCreateImageForm, AdminUpdateImageForm


LOG = logging.getLogger(__name__)

class IndexView(tables.DataTableView):
    table_class = AdminImagesTable
    template_name = 'admin/physical_servers/index.html'

    def has_more_data(self, table):
        return self._more

    def get_data(self):
        images = []
        marker = self.request.GET.get(AdminImagesTable._meta.pagination_param,
                                      None)
        try:
            images, self._more = api.glance.image_list_detailed(self.request,
                                                                marker=marker,
                                                                paginate=True)
        except:
            self._more = False
            msg = _('Unable to retrieve image list.')
            exceptions.handle(self.request, msg)
        return images

class CreateView(views.CreateView):
    template_name = 'admin/images/create.html'
    form_class = AdminCreateImageForm
    success_url = reverse_lazy('horizon:admin:images:index')


class UpdateView(views.UpdateView):
    template_name = 'admin/images/update.html'
    form_class = AdminUpdateImageForm
    success_url = reverse_lazy('horizon:admin:images:index')


class DetailView(views.DetailView):
    """ Admin placeholder for image detail view. """
    pass
