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
#   Extension for physical servers  
# Author: Dengfeng Mao
# Email:  mdengfeng@gmail.com

#[[file:$NOVA_CLIENT_ROOT$/novaclient/v1_1/contrib/physical_servers.py;action:copy]]

from novaclient import base
from novaclient import utils


class Physical_Server(base.Resource):
    def delete(self):
        self.manager.delete(model=self)


class Physical_ServerManager(base.ManagerWithFind):
    resource_class = base.Resource

    def list(self):
        return self._list('/thkcld-physical_servers', 'physical_servers')

    def get(self, physical_server):
        return self._get('/thkcld-physical_servers/%s' % base.getid(physical_server),
                         'physical_server')

    def delete(self, physical_server):
        self._delete('/thkcld-physical_servers/%s' % base.getid(physical_server))

    def create(self, user_id,server_models_id,region_id,
               locked_by,is_public,power_states_id,
               nc_number,name, description,ipmi_address,
               cpu_fre,cpu_core_num,cpu_desc,
               mem_total,mem_desc,disk_num,disk_desc,
               nic_num,nic_desc,hba_attached,
               hba_port_num,cpu_socket_num,disk_total,
               raid_internal,raid_external,hba_cards_id
               ):
        
        """
        Create a physical server.

        :param user_id: Physical server user
        :param server_models_id: server model id
        :param region_id: server location id
        :param locked_by: server was reserved by one request 
        :param is_public: the physical server resource is public or private
        :param power_states_id: server power state
        :param nic_number: the count number of nics
        :param name: server name
        :param description: description of the server
        :param ipmi_address:  server ipmi  address
        :param cpu_fre:  CPU frequence
        :param cpu_core_num: the number of cpu core
        :param cpu_desc:  description for the cpu
        :param mem_total:  total memory
        :param mem_desc:  description for the memor
        :param disk num: the number of hard disk
        :param disk_desc:  the description for the disk
        :param nic_num:  the number of nics
        :param nic_desc:  description of nics
        :param hba_attached:  the attached hba
        :param hba_port_num:    HBA port number
        :param cpu_socket_num:  the numer of cpu socket
        :param disk_total:  total disk space
        :param raid_internal:  interal raid
        :param raid_external: external raid
        :param hba_cards_id:  hba card id
        :rtype: :class:`Physcial_Server`
        """        
        body = {'physical_server':{'user_id':user_id,
                                   'server_models_id':server_models_id,
                                   'region_id':region_id,
                                   'locked_by':locked_by,
                                   'is_public':is_public,
                                   'power_states_id':power_states_id,
                                   'nc_number':nc_number,
                                   'name':name,
                                   'description':description,
                                   'ipmi_address':ipmi_address,
                                   'cpu_fre':cpu_fre,
                                   'cpu_core_num':cpu_core_num,
                                   'cpu_desc':cpu_desc,
                                   'mem_total':mem_total,
                                   'mem_desc':mem_desc,
                                   'disk_num':disk_num,
                                   'disk_desc':disk_desc,
                                   'nic_num':nic_num,
                                   'nic_desc':nic_desc,
                                   'hba_attached':hba_atached,
                                   'hba_port_num':hba_port_num,
                                   'cpu_socket_num':cpu_socket_num,
                                   'disk_total':disk_total,
                                   'raid_internal':raid_internal,
                                   'raid_external':raid_external,
                                   'hba_cards_id':hba_cards_id,                                   
                                   
                                   }}
        return self._create('/thkcld-physical_servers', body, 'server_model')


@utils.arg('physical_server_id', metavar='<physical_server_id>', help='ID of physical server')
def do_physical_server(cs, args):
    """
    Show a physical_server
    """
    physical_server = cs.physical_servers.get(args.physical_server_id)
    utils.print_dict(physical_server._info)


def do_physical_server_list(cs, args):
    """
    List physical servers
    """
    physical_servers = cs.physical_servers.list()
    utils.print_list(physical_servers, ['ID', 'Name','Description',
                                     'Server_Models_id','Power_states_id',
                                     'state'                                     
                                     ])




@utils.arg('user_id',
    metavar='<user_id>',
    help='Name of nova compute host which will control this baremetal node')
@utils.arg('server_models_id',
    metavar='<server_models_id>',
    type=int,
    help='server model id')
@utils.arg('region_id',
    metavar='<region_id>',
    type=int,
    help='server location id')
@utils.arg('locked_by',
    metavar='<locked_by>',
    type=int,
    help='Server was reserved by one request')
@utils.arg('is_public',
    metavar='<is_public>',
    help='Server is public or not')
@utils.arg('power_states_id', default=None,
    metavar='<power_states_id>',
    help='Power state id')
@utils.arg('nc_number', default=None,
    metavar='<nc_number>',
    help='Asset NC number')
@utils.arg('name', default=None,
    metavar='<name>',
    help='server name')
@utils.arg('description', default=None,
    metavar='<description>',
    help='Server description')
@utils.arg('ipmi_address', default=None,
    metavar='<ipmi_address>',
    help='Server IPMI address')
@utils.arg('cpu_fre', default=None,
    metavar='<cpu_fre>',
    help='CPU frequence')
@utils.arg('cpu_core_num', default=None,
    metavar='<cpu_core_num>',
    help='The number of CPU core')
@utils.arg('cpu_desc', default=None,
    metavar='<cpu_desc>',
    help='CPU description')
@utils.arg('mem_total', default=None,
    metavar='<mem_total>',
    help='Total memory')
@utils.arg('mem_desc', default=None,
    metavar='<mem_desc>',
    help='Memory description')
@utils.arg('disk_num', default=None,
    metavar='<disk_num>',
    help='disk number')
@utils.arg('disk_desc', default=None,
    metavar='<disk_desc>',
    help='disk description')
@utils.arg('nic_num', default=None,
    metavar='<nic_num>',
    help='nic number')
@utils.arg('nic_desc', default=None,
    metavar='<nic_desc>',
    help='nic description')
@utils.arg('hba_attached', default=None,
    metavar='<hba_attached>',
    help='hba attached')
@utils.arg('hba_port_num', default=None,
    metavar='<hba_port_num>',
    help='hba port number')
@utils.arg('cpu_socket_num', default=None,
    metavar='<cpu_socket_num>',
    help='CPU socket number')
@utils.arg('disk_total', default=None,
    metavar='<disk_total>',
    help='Disk total space')
@utils.arg('raid_internal', default=None,
    metavar='<raid_internal>',
    help='internal raid')
@utils.arg('raid_external', default=None,
    metavar='<raid_external>',
    help='external raid')
@utils.arg('hba_cards_id', default=None,
    metavar='<hba_cards_id>',
    help='HBA card id')
def do_server_model_create(cs, args):
    """
    Create a server model record
    """
    model = cs.server_models.create(args.user_id,args.server_models_id,
               args.region_id,args.locked_by,args.is_public,
               args.power_states_id,args.nc_number,args.name, 
               args.description,args.ipmi_address,args.cpu_fre,
               args.cpu_core_num,args.cpu_desc,args.mem_total,args.mem_desc,
               args.disk_num,args.disk_desc,args.nic_num,args.nic_desc,
               args.hba_attached,args.hba_port_num,args.cpu_socket_num,
               args.disk_total,args.raid_internal,args.raid_external,
               args.hba_cards_id)
    utils.print_dict(model._info)



def do_physical_server_delete(cs, args):
    """
    Delete a physical server
    """
    cs.physical_servers.delete(args.physical_server)
