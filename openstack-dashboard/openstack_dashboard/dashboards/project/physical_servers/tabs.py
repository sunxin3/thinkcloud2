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
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tabs

from openstack_dashboard import api

LOG = logging.getLogger(__name__)

class OverviewTab(tabs.Tab):
    name = _("Overview")
    slug = "overview"
    template_name = "project/physical_servers/_detail_overview.html"

    def get_context_data(self, request):
        server_id = self.tab_group.kwargs['server_id']
        try:
            server = api.nova.physical_server_get(self.request, server_id)
        except:
            redirect = reverse('horizon:project:physical_servers:index')
            exceptions.handle(request,
                              _('Unable to retrieve physical server details.'),
                              redirect=redirect)
        LOG.debug((server.rel_nic)[0]["interface"])
        return {'server': server}


class PhysicalServerDetailTabs(tabs.TabGroup):
    slug = "physical_server_details"
    tabs = (OverviewTab,)
