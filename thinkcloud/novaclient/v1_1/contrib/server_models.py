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
#   Extension for server_requests  
# Author: Dengfeng Mao
# Email:  mdengfeng@gmail.com

#[[file:$NOVA_CLIENT_ROOT$/novaclient/v1_1/contrib/server_models.py;action:copy]]
from novaclient import base
from novaclient import utils


class Server_Model(base.Resource):
    def delete(self):
        self.manager.delete(model=self)


class Server_ModelManager(base.ManagerWithFind):
    resource_class = base.Resource

    def list(self):
        return self._list('/thkcld-server_models', 'server_models')

    def get(self, server_model):
        return self._get('/thkcld-server_models/%s' % base.getid(server_model),
                         'server_model')

    def delete(self, server_model):
        self._delete('/thkcld-server_models/%s' % base.getid(server_model))

    def create(self, model_name):
        body = {'server_model':{'name':model_name}}
        return self._create('/thkcld-server_models', body, 'server_model')


@utils.arg('server_model_id', metavar='<server_model_id>', 
           help='ID of server model')
def do_server_model(cs, args):
    """
    Show a server model
    """
    server_model = cs.server_models.get(args.server_model_id)
    utils.print_dict(server_model._info)


def do_server_model_list(cs, args):
    """
    List networks
    """
    server_models = cs.server_models.list()
    utils.print_list(server_models, ['ID', 'Name','Created_at'])


@utils.arg('model_name', metavar='<model_name>',
           help='Server model name')
def do_server_model_create(cs, args):
    """
    Create a server model record
    """
    model = cs.server_models.create(args.model_name)
    utils.print_dict(model._info)


@utils.arg('server_model_id', metavar='<server_model_id>', 
           help='ID of server model')
def do_server_model_delete(cs, args):
    """
    Delete a server model
    """
    cs.server_models.delete(args.server_model_id)
