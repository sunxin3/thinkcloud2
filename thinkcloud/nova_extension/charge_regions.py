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

#[[file:$NOVA_ROOT$/nova/api/openstack/compute/contrib/charge_regions.py;action:copy]]

import webob
from webob import exc

from nova.api.openstack import wsgi
from nova import db
from nova import exception
from nova.api.openstack import extensions

authorize = extensions.extension_authorizer('compute', 'charge_regions')
 
 
 
# Controller which would response for the request
class Charge_regionsController(wsgi.Controller):
    """the Charge_region API Controller declearation"""
 
    def index(self, req):
        charge_regions = {}
        context = req.environ['nova.context']
        authorize(context)
        
        charge_regions["charge_regions"] = db.charge_region_get_all(context); 
            
        return charge_regions
    
    
 
    def create(self, req,body):
        charge_region = {}
        context = req.environ['nova.context']
        authorize(context)
        
        charge_region["charge_region"] = db.charge_region_create(context, body['charge_region'])
        return charge_region
 
 
    def show(self, req, id):
        charge_regions = {}
        context = req.environ['nova.context']
        authorize(context)
 
        try:
            charge_region = db.charge_region_get(context, id)
        except :
            raise webob.exc.HTTPNotFound(explanation="Charge_region not found")
 
        charge_regions["charge_region"] = charge_region 
        return charge_regions 
 
    def update(self, req):
        charge_regions = {}
        context = req.environ['nova.context']
        authorize(context)
 
        # real logic for update object
        return charge_regions 
 
    def delete(self, req, id):
        """Delete a charge region entry.  'id' is a region id."""
        context = req.environ['nova.context']
        authorize(context)
        num_deleted = db.charge_region_delete(context, id)
        if num_deleted == 0:
            raise exc.HTTPNotFound()
        return webob.Response(status_int=202)
    
# extension declaration 
class Charge_regions(extensions.ExtensionDescriptor):  
    """Charge_region Extension Descriptor implementation"""
 
    name = "charge_regions"
    alias = "thkcld-charge_regions"
    namespace = "http://www.thinkcloud.com/ext/api/v1.0/thkcld-charge_regions"
    updated = "2013-11-25T00:00:00+00:00"
 
    def get_resources(self):
        """register the new Charge_regions Restful resource"""
 
        resources = [extensions.ResourceExtension(self.alias,
                 Charge_regionsController())
                 ]
 
        return resources
