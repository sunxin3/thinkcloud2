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
#   Extension for charge_payment_types 
# Author: Xin Sun
# Email:  hydra_nicho@sohu.com

#[[file:$NOVA_CLIENT_ROOT$/novaclient/v1_1/contrib/charge_payment_types.py;action:copy]]
from novaclient import base
from novaclient import utils


class Charge_Payment_type(base.Resource):
    def delete(self):
        self.manager.delete(model=self)


class Charge_Payment_typeManager(base.ManagerWithFind):
    resource_class = base.Resource

    def list(self):
        return self._list('/thkcld-charge_payment_types', 'charge_payment_types')

    def get(self, charge_payment_type):
        return self._get('/thkcld-charge_payment_types/%s' % base.getid(charge_payment_type),
                         'charge_payment_type')

    def delete(self, charge_payment_type):
        self._delete('/thkcld-charge_payment_types/%s' % base.getid(charge_payment_type))

    def create(self,
               payment_type_name,
               payment_type_interval_unit,
               payment_type_interval_size,
               payment_type_is_prepaid):
        body = {'charge_payment_type': {'name': payment_type_name,
					'interval_unit': payment_type_interval_unit,
					'interval_size': payment_type_interval_size,
                                        'is_prepaid': payment_type_is_prepaid}}
        return self._create('/thkcld-charge_payment_types', body, 'charge_payment_type')


@utils.arg('charge_payment_type_id', metavar='<charge_payment_type_id>', 
           help='ID of charge payment_type')
def do_charge_payment_type(cs, args):
    """
    Show a charge payment_type
    """
    charge_payment_type = cs.charge_payment_types.get(args.charge_payment_type_id)
    utils.print_dict(charge_payment_type._info)


def do_charge_payment_type_list(cs, args):
    """
    List charge payment_types
    """
    charge_payment_types = cs.charge_payment_types.list()
    utils.print_list(charge_payment_types, ['ID', 'Name','Created_at'])


@utils.arg('payment_type_name', metavar='<payment_type_name>',
           help='Charge payment_type name')
@utils.arg('payment_type_interval_unit', metavar='<payment_type_interval_unit>',
           help='Charge payment_type interval_unit')
@utils.arg('payment_type_interval_size', metavar='<payment_type_interval_size>',
           help='Charge payment_type interval_size')
@utils.arg('payment_type_is_prepaid', metavar='<payment_type_is_prepaid>',
           help='Charge payment_type is_prepaid')
def do_charge_payment_type_create(cs, args):
    """
    Create a charge payment_type record
    """
    payment_type = cs.charge_payment_types.create(args.payment_type_name, args.payment_type_interval_unit,
               	    args.payment_type_interval_size,
                    args.payment_type_is_prepaid)
    utils.print_dict(payment_type._info)


@utils.arg('charge_payment_type_id', metavar='<charge_payment_type_id>', 
           help='ID of charge payment_type')
def do_charge_payment_type_delete(cs, args):
    """
    Delete a charge payment_type
    """
    cs.charge_payment_types.delete(args.charge_payment_type_id)
