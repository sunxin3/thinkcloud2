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
from datetime import *

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
        # authorized, don't allow the action. filters
        return False

class ApplyPhysicalServer(tables.BatchAction):
    name = "apply"
    action_present = _("Apply")
    action_past = _("Scheduled application of")
    data_type_singular = _("Physical Server")
    data_type_plural = _("Physical Servers")
    def allowed(self, request, server=None):
        return True 

    def action(self, request, obj_id):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	charge_product_id = None
	charge_products = api.nova.charge_product_list(request)
        for charge_product in charge_products:
	    if charge_product.item_name == 'physical_server':
		charge_product_id = charge_product.id

	resource_displayname = api.nova.physical_server_get(request, obj_id).name

        api.nova.charge_subscription_create(request, status='apply', product_id=charge_product_id,resource_uuid=obj_id,user_id=request.user.id, project_id=request.user.tenant_id, resource_name=resource_displayname, applied_at=now)

def filter_tenants():
    return getattr(settings, 'IMAGES_LIST_FILTER_TENANTS', [])


@memoized
def filter_tenant_ids():
    return map(lambda ft: ft['tenant'], filter_tenants())



class UpdateRow(tables.Row):
    ajax = True

    def get_data(self, request, server_id):
        server = api.nova.physical_server_get(request, server_id)
        return server

    def load_cells(self, server=None):
        super(UpdateRow, self).load_cells(server)
        # Tag the row with the server category for client-side filtering.
        server = self.datum
        my_tenant_id = self.table.request.user.tenant_id
        server_categories = get_server_categories(server, my_tenant_id)
        for category in server_categories:
            self.classes.append('category-' + category)
      
class OwnerFilter(tables.FixedFilterAction):
    def get_fixed_buttons(self):
        def make_dict(text, tenant, icon):
            return dict(text=text, value=tenant, icon=icon)
        buttons = [make_dict('Reserved by Me', 'reserved', 'icon-star')]
        buttons.append(make_dict('Free Available', 'free', 'icon-home'))
      
        return buttons

    def categorize(self, table, servers):
        user_tenant_id = table.request.user.tenant_id
        tenants = defaultdict(list)
        for server in servers:
            categories = get_server_categories(server,user_tenant_id)
            for category in categories:
                if category == "free":
                    server.ipmi_address = "N/A"
                tenants[category].append(server)
        return tenants
    
def get_server_categories(server,user_tenant_id):
    categories = []
    if server.is_public: 
        if server.subscription_id == None:
            categories.append('free')
        elif server.subscrib_project_id == user_tenant_id:
            categories.append('reserved')
    else:
        if server.subscription_id == None: 
            categories.append('private_free')
        else:
            categories.append('private_reserved')
    return categories

def  total_memory(server):
    return _("%sGB") % server.ram_sum

def  total_disk(server):
    return _("%sT") % server.disk_sum




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
    
    nics    = tables.Column("nic_sum", verbose_name=_("Nics"),
                            filters=(filters.linebreaksbr,))

    class Meta:
        name = "physicalservers"
        row_class = UpdateRow
        verbose_name = _("Physical Servers")
        # Hide the image_type column. Done this way so subclasses still get
        # all the columns by default.
        columns = ["name","nc_num" "model", "cpu","memory","storage","nics","status","ipmi", ]
        table_actions = (OwnerFilter,ApplyPhysicalServer)

