# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Copyright 2013 Think Cloud
# Copyright 2013 Lenovo Corp.
# All Rights Reserved.
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
# Description:
#   Extension for charge_subscriptions 
# Author: Xin Sun
# Email:  hydra_nicho@sohu.com

#[[file:$NOVA_CLIENT_ROOT$/novaclient/v1_1/contrib/charge_subscriptions.py;action:copy]]
from novaclient import base
from novaclient import utils


class Charge_Subscription(base.Resource):
    def delete(self):
        self.manager.delete(model=self)


class Charge_SubscriptionManager(base.ManagerWithFind):
    resource_class = base.Resource

    def list(self):
        return self._list('/thkcld-charge_subscriptions', 'charge_subscriptions')

    def get(self, charge_subscription):
        return self._get('/thkcld-charge_subscriptions/%s' % base.getid(charge_subscription),
                         'charge_subscription')

    def delete(self, charge_subscription):
        self._delete('/thkcld-charge_subscriptions/%s' % base.getid(charge_subscription))

    def create(self, subscription_name):
        body = {'charge_subscription':{'name':subscription_name}}
        return self._create('/thkcld-charge_subscriptions', body, 'charge_subscription')


@utils.arg('charge_subscription_id', metavar='<charge_subscription_id>', 
           help='ID of charge subscription')
def do_charge_subscription(cs, args):
    """
    Show a charge subscription
    """
    charge_subscription = cs.charge_subscriptions.get(args.charge_subscription_id)
    utils.print_dict(charge_subscription._info)


def do_charge_subscription_list(cs, args):
    """
    List charge subscriptions
    """
    charge_subscriptions = cs.charge_subscriptions.list()
    utils.print_list(charge_subscriptions, ['ID', 'Name','Created_at'])


@utils.arg('subscription_name', metavar='<subscription_name>',
           help='Charge subscription name')
def do_charge_subscription_create(cs, args):
    """
    Create a charge subscription record
    """
    subscription = cs.charge_subscriptions.create(args.subscription_name)
    utils.print_dict(subscription._info)


@utils.arg('charge_subscription_id', metavar='<charge_subscription_id>', 
           help='ID of charge subscription')
def do_charge_subscription_delete(cs, args):
    """
    Delete a charge subscription
    """
    cs.charge_subscriptions.delete(args.charge_subscription_id)
