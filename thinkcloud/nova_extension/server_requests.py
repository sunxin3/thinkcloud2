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

#[[file:$NOVA_ROOT$/nova/api/openstack/compute/contrib/server_requests.py;action:copy]]

import webob
from webob import exc

from nova.api.openstack import wsgi
from nova import db
from nova import exception
from nova.api.openstack import extensions

authorize = extensions.extension_authorizer('compute', 'server_requests')
 
# Controller which would response for the request
class Server_requestsController(wsgi.Controller):
    """the Server_request API Controller declearation"""
 
    def index(self, req):
        import pdb; pdb.set_trace()
        server_requests = {}
        context = req.environ['nova.context']
        authorize(context)
             
        # logic for get all records from db
       
        return server_requests 
 
    def create(self, req):
        server_requests = {}
        context = req.environ['nova.context']
        authorize(context)
 
        # real logic to create the object
        return server_requests 
 
    def show(self, req, id):
        server_requests = {}
        context = req.environ['nova.context']
        authorize(context)
 
        try:
            server_request = db.server_request_get(context, id)
        except :
            raise webob.exc.HTTPNotFound(explanation="Server_request not found")
 
        server_requests["server_request"] = server_request 
        return server_requests 
 
    def update(self, req):
        server_requests = {}
        context = req.environ['nova.context']
        authorize(context)
 
        # real logic for update object
        return server_requests 
 
    def delete(self, req, id):
        return webob.Response(status_int=202)
    
# extension declaration 
class Server_requests(extensions.ExtensionDescriptor):  
    """Server_request Extension Descriptor implementation"""
 
    name = "server_requests"
    alias = "thkcld-server_requests"
    namespace = "http://www.thinkcloud.com/ext/api/v1.0/thkcld-server_requests"
    updated = "2013-11-25T00:00:00+00:00"
 
    def get_resources(self):
        """register the new Server_requests Restful resource"""
 
        resources = [extensions.ResourceExtension(self.alias,
                 Server_requestsController())
                 ]
 
        return resources
