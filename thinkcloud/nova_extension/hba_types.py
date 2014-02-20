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
#   Extension for hba_types  
# Author: Dengfeng Mao
# Email:  mdengfeng@gmail.com

#[[file:$NOVA_ROOT$/nova/api/openstack/compute/contrib/hba_types.py;action:copy]]

import webob
from webob import exc

from nova.api.openstack import wsgi
from nova import db
from nova import exception
from nova.api.openstack import extensions

authorize = extensions.extension_authorizer('compute', 'hba_types')
 
# Controller which would response for the request
class Hba_typesController(wsgi.Controller):
    """the Hba_type API Controller declearation"""
 
    def index(self, req):
        hba_types = {}
        context = req.environ['nova.context']
        authorize(context)
             
        # logic for get all records from db
       
        return hba_types 
 
    def create(self, req):
        hba_types = {}
        context = req.environ['nova.context']
        authorize(context)
 
        # real logic to create the object
        return hba_types 
 
    def show(self, req, id):
        hba_types = {}
        context = req.environ['nova.context']
        authorize(context)
 
        try:
            hba_type = db.hba_type_get(context, id)
        except :
            raise webob.exc.HTTPNotFound(explanation="Hba_type not found")
 
        hba_types["hba_type"] = hba_type 
        return hba_types 
 
    def update(self, req):
        hba_types = {}
        context = req.environ['nova.context']
        authorize(context)
 
        # real logic for update object
        return hba_types 
 
    def delete(self, req, id):
        return webob.Response(status_int=202)
    
# extension declaration 
class Hba_types(extensions.ExtensionDescriptor):  
    """Hba_type Extension Descriptor implementation"""
 
    name = "hba_types"
    alias = "thkcld-hba_types"
    namespace = "http://www.thinkcloud.com/ext/api/v1.0/thkcld-hba_types"
    updated = "2013-11-25T00:00:00+00:00"
 
    def get_resources(self):
        """register the new Hba_types Restful resource"""
 
        resources = [extensions.ResourceExtension(self.alias,
                 Hba_typesController())
                 ]
 
        return resources
