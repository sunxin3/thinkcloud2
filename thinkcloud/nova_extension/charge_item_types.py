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

#[[file:$NOVA_ROOT$/nova/api/openstack/compute/contrib/charge_item_types.py;action:copy]]

import webob
from webob import exc

from nova.api.openstack import wsgi
from nova import db
from nova import exception
from nova.api.openstack import extensions

authorize = extensions.extension_authorizer('compute', 'charge_item_types')
 
 
 
# Controller which would response for the request
class Charge_item_typesController(wsgi.Controller):
    """the Charge_item_type API Controller declearation"""
 
    def index(self, req):
        charge_item_types = {}
        context = req.environ['nova.context']
        authorize(context)
        
        charge_item_types["charge_item_types"] = db.charge_item_type_get_all(context); 
            
        return charge_item_types
    
    
 
    def create(self, req,body):
        charge_item_type = {}
        context = req.environ['nova.context']
        authorize(context)
        
        charge_item_type["charge_item_type"] = db.charge_item_type_create(context, body['charge_item_type'])
        return charge_item_type
 
 
    def show(self, req, id):
        charge_item_types = {}
        context = req.environ['nova.context']
        authorize(context)
 
        try:
            charge_item_type = db.charge_item_type_get(context, id)
        except :
            raise webob.exc.HTTPNotFound(explanation="Charge_item_type not found")
 
        charge_item_types["charge_item_type"] = charge_item_type 
        return charge_item_types 
 
    def update(self, req):
        charge_item_types = {}
        context = req.environ['nova.context']
        authorize(context)
 
        # real logic for update object
        return charge_item_types 
 
    def delete(self, req, id):
        """Delete a charge item_type entry.  'id' is a item_type id."""
        context = req.environ['nova.context']
        authorize(context)
        num_deleted = db.charge_item_type_delete(context, id)
        if num_deleted == 0:
            raise exc.HTTPNotFound()
        return webob.Response(status_int=202)
    
# extension declaration 
class Charge_item_types(extensions.ExtensionDescriptor):  
    """Charge_item_type Extension Descriptor implementation"""
 
    name = "charge_item_types"
    alias = "thkcld-charge_item_types"
    namespace = "http://www.thinkcloud.com/ext/api/v1.0/thkcld-charge_item_types"
    updated = "2013-11-25T00:00:00+00:00"
 
    def get_resources(self):
        """register the new Charge_item_types Restful resource"""
 
        resources = [extensions.ResourceExtension(self.alias,
                 Charge_item_typesController())
                 ]
 
        return resources
