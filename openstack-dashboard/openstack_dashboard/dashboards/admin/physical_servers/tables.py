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

from django.utils.translation import ugettext_lazy as _

from horizon import tables

from openstack_dashboard.dashboards.project.physical_servers\
        .tables import (PhysicalserversTable, AddPhysicalServer, \
                       EditPhysicalServer,  DeletePhysicalServer)


class AdminAddPhysicalServer(AddPhysicalServer):
    url = "horizon:admin:images:create"


class AdminDeletePhysicalServer(DeletePhysicalServer):
    def allowed(self, request, image=None):
        return True


class AdminEditPhysicalServer(EditPhysicalServer):
    url = "horizon:admin:images:update"

    def allowed(self, request, image=None):
        return True


class AdminPhysicalserversTable(PhysicalserversTable):
    name = tables.Column("name",
                         link="horizon:admin:physical_servers:detail",
                         verbose_name=_("Server Name"))

    class Meta:
        name = "physicalservers"
        verbose_name = _("Physical Servers")
        table_actions = (AdminAddPhysicalServer, AdminDeletePhysicalServer)
        row_actions = (AdminEditPhysicalServer, AdminDeletePhysicalServer)
