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
#   Extension for charge_purchases  
# Author: Xin Sun
# Email:  hydra_nicho@sohu.com

#[[file:$NOVA_ROOT$/nova/api/openstack/compute/contrib/charge_purchases.py;action:copy]]

import webob
from webob import exc

from nova.api.openstack import wsgi
from nova import db
from nova import exception
from nova.api.openstack import extensions

authorize = extensions.extension_authorizer('compute', 'charge_purchases')
 
 
 
# Controller which would response for the request
class Charge_purchasesController(wsgi.Controller):
    """the Charge_purchase API Controller declearation"""
 
    def index(self, req):
        charge_purchases = {}
        context = req.environ['nova.context']
        authorize(context)
        
        charge_purchases["charge_purchases"] = db.charge_purchase_get_all(context); 
            
        return charge_purchases
    
    
 
    def create(self, req,body):
        charge_purchase = {}
        context = req.environ['nova.context']
        authorize(context)
        
        charge_purchase["charge_purchase"] = db.charge_purchase_create(context, body['charge_purchase'])
        return charge_purchase
 
 
    def show(self, req, id):
        charge_purchases = {}
        context = req.environ['nova.context']
        authorize(context)
 
        try:
            charge_purchase = db.charge_purchase_get(context, id)
        except :
            raise webob.exc.HTTPNotFound(explanation="Charge_purchase not found")
 
        charge_purchases["charge_purchase"] = charge_purchase 
        return charge_purchases 
 
    def update(self, req):
        charge_purchases = {}
        context = req.environ['nova.context']
        authorize(context)
 
        # real logic for update object
        return charge_purchases 
 
    def delete(self, req, id):
        """Delete a charge purchase entry.  'id' is a purchase id."""
        context = req.environ['nova.context']
        authorize(context)
        num_deleted = db.charge_purchase_delete(context, id)
        if num_deleted == 0:
            raise exc.HTTPNotFound()
        return webob.Response(status_int=202)
    
# extension declaration 
class Charge_purchases(extensions.ExtensionDescriptor):  
    """Charge_purchase Extension Descriptor implementation"""
 
    name = "charge_purchases"
    alias = "thkcld-charge_purchases"
    namespace = "http://www.thinkcloud.com/ext/api/v1.0/thkcld-charge_purchases"
    updated = "2013-11-25T00:00:00+00:00"
 
    def get_resources(self):
        """register the new Charge_purchases Restful resource"""
 
        resources = [extensions.ResourceExtension(self.alias,
                 Charge_purchasesController())
                 ]
 
        return resources
