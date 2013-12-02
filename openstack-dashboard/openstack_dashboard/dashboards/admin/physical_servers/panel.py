from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.admin import dashboard


class Physical_Servers(horizon.Panel):
    name = _("Physical Servers")
    slug = "physical_servers"


dashboard.Admin.register(Physical_Servers)
