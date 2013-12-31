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
#   Extension for charge_purchases 
# Author: Xin Sun
# Email:  hydra_nicho@sohu.com

#[[file:$NOVA_CLIENT_ROOT$/novaclient/v1_1/contrib/charge_purchases.py;action:copy]]
from novaclient import base
from novaclient import utils


class Charge_Purchase(base.Resource):
    def delete(self):
        self.manager.delete(model=self)


class Charge_PurchaseManager(base.ManagerWithFind):
    resource_class = base.Resource

    def list(self):
        return self._list('/thkcld-charge_purchases', 'charge_purchases')

    def get(self, charge_purchase):
        return self._get('/thkcld-charge_purchases/%s' % base.getid(charge_purchase),
                         'charge_purchase')

    def delete(self, charge_purchase):
        self._delete('/thkcld-charge_purchases/%s' % base.getid(charge_purchase))

    def create(self, purchase_name):
        body = {'charge_purchase':{'name':purchase_name}}
        return self._create('/thkcld-charge_purchases', body, 'charge_purchase')


@utils.arg('charge_purchase_id', metavar='<charge_purchase_id>', 
           help='ID of charge purchase')
def do_charge_purchase(cs, args):
    """
    Show a charge purchase
    """
    charge_purchase = cs.charge_purchases.get(args.charge_purchase_id)
    utils.print_dict(charge_purchase._info)


def do_charge_purchase_list(cs, args):
    """
    List charge purchases
    """
    charge_purchases = cs.charge_purchases.list()
    utils.print_list(charge_purchases, ['ID', 'Name','Created_at'])


@utils.arg('purchase_name', metavar='<purchase_name>',
           help='Charge purchase name')
def do_charge_purchase_create(cs, args):
    """
    Create a charge purchase record
    """
    purchase = cs.charge_purchases.create(args.purchase_name)
    utils.print_dict(purchase._info)


@utils.arg('charge_purchase_id', metavar='<charge_purchase_id>', 
           help='ID of charge purchase')
def do_charge_purchase_delete(cs, args):
    """
    Delete a charge purchase
    """
    cs.charge_purchases.delete(args.charge_purchase_id)
