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
#   Extension for nics  
# Author: Dengfeng Mao
# Email:  mdengfeng@gmail.com

#[[file:$NOVA_ROOT$/nova/api/openstack/compute/contrib/nics.py;action:copy]]

import webob
from webob import exc

from nova.api.openstack import wsgi
from nova import db
from nova import exception
from nova.api.openstack import extensions

authorize = extensions.extension_authorizer('compute', 'nics')
 
# Controller which would response for the request
class NicsController(wsgi.Controller):
    """the Nic API Controller declearation"""
 
    def index(self, req):
        nics = {}
        context = req.environ['nova.context']
        authorize(context)
             
        # logic for get all records from db
       
        return nics 
 
    def create(self, req):
        nics = {}
        context = req.environ['nova.context']
        authorize(context)
 
        # real logic to create the object
        return nics 
 
    def show(self, req, id):
        nics = {}
        context = req.environ['nova.context']
        authorize(context)
 
        try:
            nic = db.nic_get(context, id)
        except :
            raise webob.exc.HTTPNotFound(explanation="Nic not found")
 
        nics["nic"] = nic 
        return nics 
 
    def update(self, req):
        nics = {}
        context = req.environ['nova.context']
        authorize(context)
 
        # real logic for update object
        return nics 
 
    def delete(self, req, id):
        return webob.Response(status_int=202)
    
# extension declaration 
class Nics(extensions.ExtensionDescriptor):  
    """Nic Extension Descriptor implementation"""
 
    name = "nics"
    alias = "thkcld-nics"
    namespace = "http://www.thinkcloud.com/ext/api/v1.0/thkcld-nics"
    updated = "2013-11-25T00:00:00+00:00"
 
    def get_resources(self):
        """register the new Nics Restful resource"""
 
        resources = [extensions.ResourceExtension(self.alias,
                 NicsController())
                 ]
 
        return resources
