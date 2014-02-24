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
#   Extension for physical_servers  
# Author: Dengfeng Mao
# Email:  mdengfeng@gmail.com

#[[file:$NOVA_ROOT$/nova/api/openstack/compute/contrib/physical_servers.py;action:copy]]

import webob
from webob import exc

from nova.api.openstack import wsgi
from nova import db
from nova import exception
from nova.api.openstack import extensions
from nova.openstack.common import log as logging

LOG = logging.getLogger(__name__)
authorize = extensions.extension_authorizer('compute', 'physical_servers')
 
# Controller which would response for the request
class Physical_serversController(wsgi.Controller):
    """the Physical_server API Controller declearation"""
 
    def index(self, req):
        physical_servers = {}
        context = req.environ['nova.context']
        authorize(context)
              
        physical_servers["physical_servers"] = db.physical_server_get_all(context)
       
        return physical_servers 
    
 
    def create(self, req):
        physical_servers = {}
        context = req.environ['nova.context']
        authorize(context)
 
        # real logic to create the object
        return physical_servers 
 
    def show(self, req, id):
        physical_servers = {}
        context = req.environ['nova.context']
        authorize(context)
 
        try:
            physical_server = db.physical_server_get(context, id)
        except :
            raise webob.exc.HTTPNotFound(explanation="Physical_server not found")
 
        physical_servers["physical_server"] = physical_server 
        return physical_servers 
 
    def update(self, req):
        physical_servers = {}
        context = req.environ['nova.context']
        authorize(context)
 
        # real logic for update object
        return physical_servers 
 
    def delete(self, req, id):
        
        context = req.environ['nova.context']
        authorize(context)

        LOG.debug(_("Delete physical server with id: %s"), id, context=context)

        rows_deleted = db.physical_server_delete(context, id)
        LOG.debug(_("Delete physical server rows: %s"), rows_deleted, context=context)
        if rows_deleted == 0:
            raise exc.HTTPNotFound()
        return webob.Response(status_int=202)
        
    
    
# extension declaration 
class Physical_servers(extensions.ExtensionDescriptor):  
    """Physical_server Extension Descriptor implementation"""
 
    name = "physical_servers"
    alias = "thkcld-physical_servers"
    namespace = "http://www.thinkcloud.com/ext/api/v1.0/thkcld-physical_servers"
    updated = "2013-11-25T00:00:00+00:00"
 
    def get_resources(self):
        """register the new Physical_servers Restful resource"""
 
        resources = [extensions.ResourceExtension(self.alias,
                 Physical_serversController())
                 ]
 
        return resources
