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
#   Extension for charge_item_types 
# Author: Xin Sun
# Email:  hydra_nicho@sohu.com

#[[file:$NOVA_CLIENT_ROOT$/novaclient/v1_1/contrib/charge_item_types.py;action:copy]]
from novaclient import base
from novaclient import utils


class Charge_Item_type(base.Resource):
    def delete(self):
        self.manager.delete(model=self)


class Charge_Item_typeManager(base.ManagerWithFind):
    resource_class = base.Resource

    def list(self):
        return self._list('/thkcld-charge_item_types', 'charge_item_types')

    def get(self, charge_item_type):
        return self._get('/thkcld-charge_item_types/%s' % base.getid(charge_item_type),
                         'charge_item_type')

    def delete(self, charge_item_type):
        self._delete('/thkcld-charge_item_types/%s' % base.getid(charge_item_type))

    def create(self, item_type_name):
        body = {'charge_item_type':{'name':item_type_name}}
        return self._create('/thkcld-charge_item_types', body, 'charge_item_type')


@utils.arg('charge_item_type_id', metavar='<charge_item_type_id>', 
           help='ID of charge item_type')
def do_charge_item_type(cs, args):
    """
    Show a charge item_type
    """
    charge_item_type = cs.charge_item_types.get(args.charge_item_type_id)
    utils.print_dict(charge_item_type._info)


def do_charge_item_type_list(cs, args):
    """
    List charge item_types
    """
    charge_item_types = cs.charge_item_types.list()
    utils.print_list(charge_item_types, ['ID', 'Name','Created_at'])


@utils.arg('item_type_name', metavar='<item_type_name>',
           help='Charge item_type name')
def do_charge_item_type_create(cs, args):
    """
    Create a charge item_type record
    """
    item_type = cs.charge_item_types.create(args.item_type_name)
    utils.print_dict(item_type._info)


@utils.arg('charge_item_type_id', metavar='<charge_item_type_id>', 
           help='ID of charge item_type')
def do_charge_item_type_delete(cs, args):
    """
    Delete a charge item_type
    """
    cs.charge_item_types.delete(args.charge_item_type_id)
