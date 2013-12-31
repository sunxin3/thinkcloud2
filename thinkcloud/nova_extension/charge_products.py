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
#   Extension for charge_products  
# Author: Xin Sun
# Email:  hydra_nicho@sohu.com

#[[file:$NOVA_ROOT$/nova/api/openstack/compute/contrib/charge_products.py;action:copy]]

import webob
from webob import exc

from nova.api.openstack import wsgi
from nova import db
from nova import exception
from nova.api.openstack import extensions

authorize = extensions.extension_authorizer('compute', 'charge_products')
 
 
 
# Controller which would response for the request
class Charge_productsController(wsgi.Controller):
    """the Charge_product API Controller declearation"""
 
    def index(self, req):
        charge_products = {}
        context = req.environ['nova.context']
        authorize(context)
        
        charge_products["charge_products"] = db.charge_product_get_all(context); 
            
        return charge_products
    
    
 
    def create(self, req,body):
        charge_product = {}
        context = req.environ['nova.context']
        authorize(context)
        
        charge_product["charge_product"] = db.charge_product_create(context, body['charge_product'])
        return charge_product
 
 
    def show(self, req, id):
        charge_products = {}
        context = req.environ['nova.context']
        authorize(context)
 
        try:
            charge_product = db.charge_product_get(context, id)
        except :
            raise webob.exc.HTTPNotFound(explanation="Charge_product not found")
 
        charge_products["charge_product"] = charge_product 
        return charge_products 
 
    def update(self, req):
        charge_products = {}
        context = req.environ['nova.context']
        authorize(context)
 
        # real logic for update object
        return charge_products 
 
    def delete(self, req, id):
        """Delete a charge product entry.  'id' is a product id."""
        context = req.environ['nova.context']
        authorize(context)
        num_deleted = db.charge_product_delete(context, id)
        if num_deleted == 0:
            raise exc.HTTPNotFound()
        return webob.Response(status_int=202)
    
# extension declaration 
class Charge_products(extensions.ExtensionDescriptor):  
    """Charge_product Extension Descriptor implementation"""
 
    name = "charge_products"
    alias = "thkcld-charge_products"
    namespace = "http://www.thinkcloud.com/ext/api/v1.0/thkcld-charge_products"
    updated = "2013-11-25T00:00:00+00:00"
 
    def get_resources(self):
        """register the new Charge_products Restful resource"""
 
        resources = [extensions.ResourceExtension(self.alias,
                 Charge_productsController())
                 ]
 
        return resources
