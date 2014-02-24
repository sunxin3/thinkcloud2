# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 Openstack, LLC
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

from django.template.defaultfilters import title
from django.utils.translation import ugettext_lazy as _

from horizon import tables
from horizon.utils.filters import replace_underscores

from openstack_dashboard import api
from openstack_dashboard.dashboards.project.charge_subscriptions.tables import (
	ApproveChargeSubscription, DenyChargeSubscription,
        get_size, UpdateRow,
        get_power_state, is_deleting, ACTIVE_STATES, STATUS_DISPLAY_CHOICES,
        TASK_DISPLAY_CHOICES)

LOG = logging.getLogger(__name__)


class MigrateInstance(tables.BatchAction):
    name = "migrate"
    action_present = _("Migrate")
    action_past = _("Scheduled migration (pending confirmation) of")
    data_type_singular = _("Instance")
    data_type_plural = _("Instances")
    classes = ("btn-migrate", "btn-danger")

    def allowed(self, request, instance):
        return ((instance.status in ACTIVE_STATES
                 or instance.status == 'SHUTOFF')
                and not is_deleting(instance))

    def action(self, request, obj_id):
        api.nova.server_migrate(request, obj_id)


class AdminUpdateRow(UpdateRow):
    def get_data(self, request, instance_id):
        instance = super(AdminUpdateRow, self).get_data(request, instance_id)
        tenant = api.keystone.tenant_get(request,
                                         instance.tenant_id,
                                         admin=True)
        instance.tenant_name = getattr(tenant, "name", None)
        return instance


class AdminChargesTable(tables.DataTable):
    TASK_STATUS_CHOICES = (
        (None, True),
        ("none", True)
    )
    STATUS_CHOICES = (
        ("active", True),
        ("shutoff", True),
        ("suspended", True),
        ("paused", True),
        ("error", False),
    )

    def get_object_display(self, datum):
        return datum.resource_name

    item = tables.Column("item",
                            verbose_name=_("Charge Product"))

    resource = tables.Column("resource_name",
                             verbose_name=_("Resource Name"))

    resource_uuid = tables.Column("resource_uuid",
                             verbose_name=_("Resource UUID"))

    user = tables.Column("user_id",
                             verbose_name=_("Applyer"))

    approver = tables.Column("approver_id",
                             verbose_name=_("Approver"))

    status = tables.Column("status",
                           filters=(title, replace_underscores),
			   verbose_name=_("Status"),
                           status=True,
                           status_choices=STATUS_CHOICES,
                           display_choices=STATUS_DISPLAY_CHOICES)

    applied_at = tables.Column("applied_at",
                            verbose_name=_("Apply Time"))

    approved_at = tables.Column("approved_at",
                            verbose_name=_("Approved Time"))

    expires_at = tables.Column("expires_at",
                            verbose_name=_("Expires Time"))

    class Meta:
        name = "instances"
        verbose_name = _("Instances")
        status_columns = ["status"]
        table_actions = (ApproveChargeSubscription, DenyChargeSubscription)
        row_class = AdminUpdateRow
