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
#   Extension for charge_regions 
# Author: Xin Sun
# Email:  hydra_nicho@sohu.com

#[[file:$NOVA_CLIENT_ROOT$/novaclient/v1_1/contrib/charge_regions.py;action:copy]]
from novaclient import base
from novaclient import utils


class Charge_Region(base.Resource):
    def delete(self):
        self.manager.delete(model=self)


class Charge_RegionManager(base.ManagerWithFind):
    resource_class = base.Resource

    def list(self):
        return self._list('/thkcld-charge_regions', 'charge_regions')

    def get(self, charge_region):
        return self._get('/thkcld-charge_regions/%s' % base.getid(charge_region),
                         'charge_region')

    def delete(self, charge_region):
        self._delete('/thkcld-charge_regions/%s' % base.getid(charge_region))

    def create(self, region_name):
        body = {'charge_region':{'name':region_name}}
        return self._create('/thkcld-charge_regions', body, 'charge_region')


@utils.arg('charge_region_id', metavar='<charge_region_id>', 
           help='ID of charge region')
def do_charge_region(cs, args):
    """
    Show a charge region
    """
    charge_region = cs.charge_regions.get(args.charge_region_id)
    utils.print_dict(charge_region._info)


def do_charge_region_list(cs, args):
    """
    List charge regions
    """
    charge_regions = cs.charge_regions.list()
    utils.print_list(charge_regions, ['ID', 'Name','Created_at'])


@utils.arg('region_name', metavar='<region_name>',
           help='Charge region name')
def do_charge_region_create(cs, args):
    """
    Create a charge region record
    """
    region = cs.charge_regions.create(args.region_name)
    utils.print_dict(region._info)


@utils.arg('charge_region_id', metavar='<charge_region_id>', 
           help='ID of charge region')
def do_charge_region_delete(cs, args):
    """
    Delete a charge region
    """
    cs.charge_regions.delete(args.charge_region_id)
