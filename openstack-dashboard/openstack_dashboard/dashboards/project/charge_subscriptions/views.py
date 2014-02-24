# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
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

"""
Views for managing charge subscriptions.
"""
import logging
import iso8601

from django import http
from django import shortcuts
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.datastructures import SortedDict
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import forms
from horizon import tabs
from horizon import tables
from horizon import workflows

from openstack_dashboard import api
from .tables import ChargeSubscriptionTable


LOG = logging.getLogger(__name__)


class IndexView(tables.DataTableView):
    table_class = ChargeSubscriptionTable
    template_name = 'project/charge_subscriptions/index.html'

    def get_data(self):
	charge_subscriptions_by_user = []
        try:
            charge_subscriptions = api.nova.charge_subscription_list(self.request)
            for charge_subscription in charge_subscriptions:
                if self.request.user.id == charge_subscription.user_id:
                    charge_subscription.user_id = api.keystone.user_get(self.request, charge_subscription.user_id).name
                    try:
                        #TODO: fixme need to test it into product envirment.
                        #TODO: fixme need to add resource_name get syncing 
                        charge_subscription.resource_uuid = api.nova.server_get(self.request, charge_subscription.resource_uuid).name
                    except:
                        pass

                    if charge_subscription.approver_id:
                        charge_subscription.approver_id = api.keystone.user_get(self.request, charge_subscription.approver_id).name
                    else:
                        charge_subscription.approver_id = 'N/A'

                    charge_subscription.applied_at = iso8601.parse_date(charge_subscription.applied_at).strftime("%Y-%m-%d %H:%M:%S")
                    charge_subscription.approved_at = iso8601.parse_date(charge_subscription.approved_at).strftime("%Y-%m-%d %H:%M:%S")
                    charge_subscription.expires_at = iso8601.parse_date(charge_subscription.expires_at).strftime("%Y-%m-%d %H:%M:%S")

                    charge_subscriptions_by_user.append(charge_subscription)
        except:
            exceptions.handle(self.request,
                              _('Unable to retrieve charge subscriptions'))
        return charge_subscriptions_by_user
