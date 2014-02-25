# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import logging
from collections import defaultdict

from django.conf import settings
from django.core.urlresolvers import reverse
from django.template import defaultfilters as filters
from django.utils.http import urlencode
from django.utils.translation import ugettext_lazy as _

from horizon import tables
from horizon.utils.memoized import memoized

from openstack_dashboard import api


LOG = logging.getLogger(__name__)



class DeletePhysicalServer(tables.DeleteAction):
    data_type_singular = _("Physical Server")
    data_type_plural = _("Physical Servers")
    def allowed(self, request, server=None):
        return False

    def delete(self, request, obj_id):
        api.nova.physical_server_delete(request, obj_id)


class AddPhysicalServer(tables.LinkAction):
    name = "create"
    verbose_name = _("Add Physical Server")
    url = "horizon:project:physical_servers:create"
    classes = ("ajax-modal", "btn-create")


class EditPhysicalServer(tables.LinkAction):
    name = "edit"
    verbose_name = _("Edit")
    url = "horizon:project:physical_servers:update"
    classes = ("ajax-modal", "btn-edit")

    def allowed(self, request, image=None):
        if image:
            return image.status in ("active",) and \
                image.owner == request.user.tenant_id
        # We don't have bulk editing, so if there isn't an image that's
        # authorized, don't allow the action.
        return False


def filter_tenants():
    return getattr(settings, 'IMAGES_LIST_FILTER_TENANTS', [])


@memoized
def filter_tenant_ids():
    return map(lambda ft: ft['tenant'], filter_tenants())



class UpdateRow(tables.Row):
    ajax = True

    def get_data(self, request, image_id):
        image = api.glance.image_get(request, image_id)
        return image

    def load_cells(self, image=None):
        super(UpdateRow, self).load_cells(image)

      
class OwnerFilter(tables.FixedFilterAction):
    def get_fixed_buttons(self):
        def make_dict(text, tenant, icon):
            return dict(text=text, value=tenant, icon=icon)

        buttons = [make_dict('Free Avaiale', 'project', 'icon-home')]
        buttons.append(make_dict('Reserved by Me', 'shared', 'icon-star'))
        buttons.append(make_dict('Power On', 'public', 'icon-play'))
        buttons.append(make_dict('Power Off', 'public', 'icon-stop'))
        return buttons

    def categorize(self, table, images):
        user_tenant_id = table.request.user.tenant_id
        tenants = defaultdict(list)
        for im in images:
            categories = [] #get_image_categories(im, user_tenant_id)
            for category in categories:
                tenants[category].append(im)
        return tenants
    
def get_server_categories(server,user_tenant_id):
    categories = []
    if server.is_public:
        categories.append('public')
    if server.owner == user_tenant_id:
        categories.append('project')
    elif server.owner in filter_tenant_ids():
        categories.append(server.owner)
    elif not server.is_public:
        categories.append('shared')
    return categories

def  total_memory(server):
    return _("%sGB") % server.ram_sum

def  total_disk(server):
    return _("%sT") % server.disk_sum

class ModelFilterAction(tables.LinkAction):
    name  = "model"
    classes = ("btn-list")
    def get_link_url(self, datum=None):
        
        return 


class PhysicalserversTable(tables.DataTable):

    name = tables.Column("name",
                         link=("horizon:project:physical_servers:"
                               "detail"),
                         verbose_name=_("Server Name"))
    nc_num = tables.Column("nc_number",
                             verbose_name=_("NC Number"))
    model = tables.Column("model",
                               verbose_name=_("Model"),
                               filters=(filters.upper,))
    status = tables.Column("state",
                           filters=(filters.title,),
                           verbose_name=_("Power State"),)
    ipmi  = tables.Column("ipmi_address",
                          verbose_name= _("IPMI Address"))
    public = tables.Column("is_public",
                           verbose_name=_("Public"),
                           empty_value=False,
                           filters=(filters.yesno, filters.capfirst))
    cpu = tables.Column("cpu_desc", verbose_name=_("Cpu"))
    
    memory = tables.Column(total_memory, verbose_name=_("Memory"))
    
    storage = tables.Column(total_disk, verbose_name=_("Storage"))
    
    nics    = tables.Column("nic_num", verbose_name=_("Nics"))

    class Meta:
        name = "physicalservers"
        status_columns = ["status"]
        verbose_name = _("Physical Servers")
        # Hide the image_type column. Done this way so subclasses still get
        # all the columns by default.
        columns = ["name","nc_num" "model","status","ipmi", "public", "cpu","memory","storage","nics"]
        table_actions = (ModelFilterAction,OwnerFilter,)

