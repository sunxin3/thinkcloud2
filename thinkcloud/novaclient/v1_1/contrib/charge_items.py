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
#   Extension for charge_items 
# Author: Xin Sun
# Email:  hydra_nicho@sohu.com

#[[file:$NOVA_CLIENT_ROOT$/novaclient/v1_1/contrib/charge_items.py;action:copy]]
from novaclient import base
from novaclient import utils


class Charge_Item(base.Resource):
    def delete(self):
        self.manager.delete(model=self)


class Charge_ItemManager(base.ManagerWithFind):
    resource_class = base.Resource

    def list(self):
        return self._list('/thkcld-charge_items', 'charge_items')

    def get(self, charge_item):
        return self._get('/thkcld-charge_items/%s' % base.getid(charge_item),
                         'charge_item')

    def delete(self, charge_item):
        self._delete('/thkcld-charge_items/%s' % base.getid(charge_item))

    def create(self, item_name):
        body = {'charge_item':{'name':item_name}}
        return self._create('/thkcld-charge_items', body, 'charge_item')


@utils.arg('charge_item_id', metavar='<charge_item_id>', 
           help='ID of charge item')
def do_charge_item(cs, args):
    """
    Show a charge item
    """
    charge_item = cs.charge_items.get(args.charge_item_id)
    utils.print_dict(charge_item._info)


def do_charge_item_list(cs, args):
    """
    List charge items
    """
    charge_items = cs.charge_items.list()
    utils.print_list(charge_items, ['ID', 'Name','Created_at'])


@utils.arg('item_name', metavar='<item_name>',
           help='Charge item name')
def do_charge_item_create(cs, args):
    """
    Create a charge item record
    """
    item = cs.charge_items.create(args.item_name)
    utils.print_dict(item._info)


@utils.arg('charge_item_id', metavar='<charge_item_id>', 
           help='ID of charge item')
def do_charge_item_delete(cs, args):
    """
    Delete a charge item
    """
    cs.charge_items.delete(args.charge_item_id)
