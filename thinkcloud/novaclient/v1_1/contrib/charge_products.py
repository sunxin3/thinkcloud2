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
#   Extension for charge_products 
# Author: Xin Sun
# Email:  hydra_nicho@sohu.com

#[[file:$NOVA_CLIENT_ROOT$/novaclient/v1_1/contrib/charge_products.py;action:copy]]
from novaclient import base
from novaclient import utils


class Charge_Product(base.Resource):
    def delete(self):
        self.manager.delete(model=self)


class Charge_ProductManager(base.ManagerWithFind):
    resource_class = base.Resource

    def list(self):
        return self._list('/thkcld-charge_products', 'charge_products')

    def get(self, charge_product):
        return self._get('/thkcld-charge_products/%s' % base.getid(charge_product),
                         'charge_product')

    def delete(self, charge_product):
        self._delete('/thkcld-charge_products/%s' % base.getid(charge_product))

    def create(self,
               product_name,
               product_interval_unit,
               product_interval_size,
               product_is_prepaid):
        body = {'charge_product': {'name': product_name,
					'interval_unit': product_interval_unit,
					'interval_size': product_interval_size,
                                        'is_prepaid': product_is_prepaid}}
        return self._create('/thkcld-charge_products', body, 'charge_product')


@utils.arg('charge_product_id', metavar='<charge_product_id>', 
           help='ID of charge product')
def do_charge_product(cs, args):
    """
    Show a charge product
    """
    charge_product = cs.charge_products.get(args.charge_product_id)
    utils.print_dict(charge_product._info)


def do_charge_product_list(cs, args):
    """
    List charge products
    """
    charge_products = cs.charge_products.list()
    utils.print_list(charge_products, ['ID', 'Name','Created_at'])


@utils.arg('product_name', metavar='<product_name>',
           help='Charge product name')
@utils.arg('product_interval_unit', metavar='<product_interval_unit>',
           help='Charge product interval_unit')
@utils.arg('product_interval_size', metavar='<product_interval_size>',
           help='Charge product interval_size')
@utils.arg('product_is_prepaid', metavar='<product_is_prepaid>',
           help='Charge product is_prepaid')
def do_charge_product_create(cs, args):
    """
    Create a charge product record
    """
    product = cs.charge_products.create(args.product_name, args.product_interval_unit,
               	    args.product_interval_size,
                    args.product_is_prepaid)
    utils.print_dict(product._info)


@utils.arg('charge_product_id', metavar='<charge_product_id>', 
           help='ID of charge product')
def do_charge_product_delete(cs, args):
    """
    Delete a charge product
    """
    cs.charge_products.delete(args.charge_product_id)
