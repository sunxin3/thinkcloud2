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
from collections import defaultdict

from django.utils.translation import ugettext_lazy as _

from horizon import tables

from openstack_dashboard import api
from openstack_dashboard.dashboards.project.physical_servers\
        .tables import (PhysicalserversTable, AddPhysicalServer, \
                       EditPhysicalServer,  DeletePhysicalServer,\
                       RebootPhysicalServer, ShutdownPhysicalServer,\
                       PublicPhysicalServer,PrivatePhysicalServer,\
                       PoweronPhysicalServer,PasswordPhysicalServer)


class AdminAddPhysicalServer(AddPhysicalServer):
    url = "horizon:admin:physical_servers:create"


class AdminDeletePhysicalServer(DeletePhysicalServer):
    def allowed(self, request, server=None):
        return True


class AdminEditPhysicalServer(EditPhysicalServer):
    url = "horizon:admin:images:update"

    def allowed(self, request, server=None):
        return True

class AdminRebootPhysicalServer(RebootPhysicalServer):
    def allowed(self, request, obj_id):
        return True

class AdminShutdownPhysicalServer(ShutdownPhysicalServer):
    def allowed(self, request, obj_id):
        return True

class AdminPoweronPhysicalServer(PoweronPhysicalServer):
    def allowed(self, request, obj_id):
        return True
    
class AdminnPasswordPhysicalServer(PasswordPhysicalServer):
    def allowed(self, request, obj_id):
        return True

class AdminPublicPhysicalServer(PublicPhysicalServer):
    def allowed(self, request, datum):
        #is_public = api.nova.physical_server_get(request, obj_id).is_public
        if not datum.is_public:
             return True
        return False
    
class AdminPrivatePhysicalServer(PrivatePhysicalServer):
    def allowed(self, request, datum):
        #is_public = api.nova.physical_server_get(request, obj_id).is_public
        if datum.is_public:
             return True
        return False
    
class AdminOwnerFilter(tables.FixedFilterAction):
    def get_fixed_buttons(self):
        def make_dict(text, user, icon):
            return dict(text=text, value=user, icon=icon)
        buttons = [make_dict('Public', 'public', 'icon-star')]
        buttons.append(make_dict('Private Reserved', 'private_reserved', 'icon-home'))
        buttons.append(make_dict('Private Free', 'private_free', 'icon-fire'))
      
        return buttons

    def categorize(self, table, servers):
        user_id = table.request.user.id
        users = defaultdict(list)
        for server in servers:
            categories = get_server_categories(server,user_id)
            for category in categories:
                users[category].append(server)
        return users

def get_server_categories(server,user_id):
    categories = []
    if server.is_public: 
        categories.append('public')
    else:
        if server.subscription_id == None: 
            categories.append('private_free')
        else:
            categories.append('private_reserved')
    return categories


class UpdateRow(tables.Row):
    ajax = True

    def get_data(self, request, server_id):
        server = api.nova.physical_server_get(request, server_id)
        return server

    def load_cells(self, server=None):
        super(UpdateRow, self).load_cells(server)
        # Tag the row with the server category for client-side filtering.
        server = self.datum
        my_user_id = self.table.request.user.id
        server_categories = get_server_categories(server, my_user_id)
        for category in server_categories:
            self.classes.append('category-' + category)
            

class AdminPhysicalserversTable(PhysicalserversTable):
    name = tables.Column("name",
                         link="horizon:admin:physical_servers:detail",
                         verbose_name=_("Server Name"))

    class Meta:
        name = "physicalservers"
        row_class = UpdateRow
        verbose_name = _("Physical Servers")
        columns = ["nc_num", "name", "model","owner","cpu","memory","storage","nics","status","ipmi","ipmi_password", "subscrib_status", ]
        table_actions = (AdminOwnerFilter,AdminAddPhysicalServer, AdminDeletePhysicalServer)
        row_actions = (AdminEditPhysicalServer, AdminDeletePhysicalServer, AdminRebootPhysicalServer, AdminShutdownPhysicalServer, AdminPoweronPhysicalServer, AdminPublicPhysicalServer, AdminPrivatePhysicalServer, AdminnPasswordPhysicalServer)
