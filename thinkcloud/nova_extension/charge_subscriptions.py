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
#   Extension for charge_subscriptions  
# Author: Xin Sun
# Email:  hydra_nicho@sohu.com

#[[file:$NOVA_ROOT$/nova/api/openstack/compute/contrib/charge_subscriptions.py;action:copy]]

import webob
from webob import exc

from nova.api.openstack import wsgi
from nova import db
from nova import exception
from nova.api.openstack import extensions

authorize = extensions.extension_authorizer('compute', 'charge_subscriptions')
 
 
 
# Controller which would response for the request
class Charge_subscriptionsController(wsgi.Controller):
    """the Charge_subscription API Controller declearation"""
 
    def index(self, req):
        charge_subscriptions = {}
        context = req.environ['nova.context']
        authorize(context)
        
        charge_subscriptions["charge_subscriptions"] = db.charge_subscription_get_all(context); 
            
        return charge_subscriptions
    
    
 
    def create(self, req, id, body):
        charge_subscription = {}
        context = req.environ['nova.context']
        authorize(context)
        
        charge_subscription["charge_subscription"] = db.charge_subscription_create(context, body['charge_subscription'])
        return charge_subscription
 
 
    def show(self, req, id):
        charge_subscriptions = {}
        context = req.environ['nova.context']
        authorize(context)
 
        try:
            charge_subscription = db.charge_subscription_get(context, id)
        except :
            raise webob.exc.HTTPNotFound(explanation="Charge_subscription not found")
 
        charge_subscriptions["charge_subscription"] = charge_subscription 
        return charge_subscriptions 
 
    def update(self, req, id, body):
        charge_subscriptions = {}
        context = req.environ['nova.context']
        authorize(context)
 
        num_updated = db.charge_subscription_update(context, id, body['charge_subscription'])
        if num_updated == 0:
            raise exc.HTTPNotFound()
        return webob.Response(status_int=202)
 
    def delete(self, req, id):
        """Delete a charge subscription entry.  'id' is a subscription id."""
        context = req.environ['nova.context']
        authorize(context)
        num_deleted = db.charge_subscription_delete(context, id)
        if num_deleted == 0:
            raise exc.HTTPNotFound()
        return webob.Response(status_int=202)
    
# extension declaration 
class Charge_subscriptions(extensions.ExtensionDescriptor):  
    """Charge_subscription Extension Descriptor implementation"""
 
    name = "charge_subscriptions"
    alias = "thkcld-charge_subscriptions"
    namespace = "http://www.thinkcloud.com/ext/api/v1.0/thkcld-charge_subscriptions"
    updated = "2013-11-25T00:00:00+00:00"
 
    def get_resources(self):
        """register the new Charge_subscriptions Restful resource"""
 
        resources = [extensions.ResourceExtension(self.alias,
                 Charge_subscriptionsController())
                 ]
 
        return resources
