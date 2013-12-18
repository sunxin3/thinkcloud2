from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.project import dashboard


class Physical_Servers(horizon.Panel):
    name = _("Physical Servers")
    slug = "physical_servers"


dashboard.Project.register(Physical_Servers)
