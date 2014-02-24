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
import types
from  datetime import * 

from django import shortcuts
from django import template
from django.core import urlresolvers
from django.template.defaultfilters import title
from django.utils.http import urlencode
from django.utils.translation import string_concat, ugettext_lazy as _

from horizon.conf import HORIZON_CONFIG
from horizon import exceptions
from horizon import messages
from horizon import tables
from horizon.templatetags import sizeformat
from horizon.utils.filters import replace_underscores

from openstack_dashboard import api


LOG = logging.getLogger(__name__)

ACTIVE_STATES = ("ACTIVE",)

POWER_STATES = {
    0: "NO STATE",
    1: "RUNNING",
    2: "BLOCKED",
    3: "PAUSED",
    4: "SHUTDOWN",
    5: "SHUTOFF",
    6: "CRASHED",
    7: "SUSPENDED",
    8: "FAILED",
    9: "BUILDING",
}

PAUSE = 0
UNPAUSE = 1
SUSPEND = 0
RESUME = 1


def is_deleting(instance):
    task_state = getattr(instance, "OS-EXT-STS:task_state", None)
    if not task_state:
        return False
    return task_state.lower() == "deleting"

class ApproveChargeSubscription(tables.BatchAction):
    name = "approve"
    action_present = _("Approve")
    action_past = _("Scheduled approval of")
    data_type_singular = _("Subscription")
    data_type_plural = _("Subscriptions")
    classes = ('btn-danger', 'btn-reboot')

    def allowed(self, request, charge_subcription=None):
        return True

    def action(self, request, obj_id):
	now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        api.nova.charge_subscription_update(request, obj_id, status='verified', approver_id=request.user.id, approved_at=now)

class DenyChargeSubscription(tables.BatchAction):
    name = "deny"
    action_present = _("Deny")
    action_past = _("Scheduled denial of")
    data_type_singular = _("Subscription")
    data_type_plural = _("Subscriptions")
    classes = ('btn-danger', 'btn-reboot')

    def allowed(self, request, charge_subcription=None):
        return True

    def action(self, request, obj_id):
        api.nova.charge_subscription_update(request, obj_id, status='denied', approver_id=request.user.id)

class UpdateRow(tables.Row):
    ajax = True

    def get_data(self, request, charge_subscription_id):
        charge_subscription = api.nova.charge_subscription_get(request, charge_subscription_id)
        return charge_subscription

def get_size(instance):
    if hasattr(instance, "full_flavor"):
        size_string = _("%(name)s | %(RAM)s RAM | %(VCPU)s VCPU "
                        "| %(disk)s Disk")
        vals = {'name': instance.full_flavor.name,
                'RAM': sizeformat.mbformat(instance.full_flavor.ram),
                'VCPU': instance.full_flavor.vcpus,
                'disk': sizeformat.diskgbformat(instance.full_flavor.disk)}
        return size_string % vals
    return _("Not available")


def get_keyname(instance):
    if hasattr(instance, "key_name"):
        keyname = instance.key_name
        return keyname
    return _("Not available")


def get_power_state(instance):
    return POWER_STATES.get(getattr(instance, "OS-EXT-STS:power_state", 0), '')


STATUS_DISPLAY_CHOICES = (
    ("resize", "Resize/Migrate"),
    ("verify_resize", "Confirm or Revert Resize/Migrate"),
    ("revert_resize", "Revert Resize/Migrate"),
)


TASK_DISPLAY_CHOICES = (
    ("image_snapshot", "Snapshotting"),
    ("resize_prep", "Preparing Resize or Migrate"),
    ("resize_migrating", "Resizing or Migrating"),
    ("resize_migrated", "Resized or Migrated"),
    ("resize_finish", "Finishing Resize or Migrate"),
    ("resize_confirming", "Confirming Resize or Nigrate"),
    ("resize_reverting", "Reverting Resize or Migrate"),
    ("unpausing", "Resuming"),
)


class ChargeSubscriptionTable(tables.DataTable):
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

    resource_name = tables.Column("resource_name",
                             verbose_name=_("Resource Name"))

    resource_uuid = tables.Column("resource_uuid",
                             verbose_name=_("Resource UUID"))

    user = tables.Column("user_id",
                             verbose_name=_("Applyer"))

    approver = tables.Column("approver_id",
                             verbose_name=_("Approver"))

    status = tables.Column("status",
                           verbose_name=_("Status"))

    applied_at = tables.Column("applied_at",
                            verbose_name=_("Apply Time"))

    approved_at = tables.Column("approved_at",
                            verbose_name=_("Approved Time"))

    expires_at = tables.Column("expires_at",
                            verbose_name=_("Expires Time"))

    class Meta:
        name = "ChargeSubscriptions"
        verbose_name = _("Charge Subscriptions")
        #status_columns = ["status", "task"]
        row_class = UpdateRow
        #table_actions = (ApproveChargeSubscription, DenyChargeSubscription)
