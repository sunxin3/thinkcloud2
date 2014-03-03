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
#   Extension for usages  
# Author: Dengfeng Mao
# Email:  mdengfeng@gmail.com

#[[file:$NOVA_ROOT$/nova/api/openstack/compute/contrib/usages.py;action:copy]]

import webob
from webob import exc

from nova.api.openstack import wsgi
from nova import db
from nova import exception
from nova.api.openstack import extensions
from nova.openstack.common import log as logging

LOG = logging.getLogger(__name__)
authorize = extensions.extension_authorizer('compute', 'usages')
 
# Controller which would response for the request
class UsagesController(wsgi.Controller):
    """the Usage API Controller declearation"""
 
    def index(self, req):
        usages = {}
        context = req.environ['nova.context']
        authorize(context)
             
        # logic for get all records from db
       
        return usages 
 
    def create(self, req):
        usages = {}
        context = req.environ['nova.context']
        authorize(context)
 
        # real logic to create the object
        return usages 
 
    def show(self, req, id):
        usages = {}
        context = req.environ['nova.context']
        authorize(context)
 
        try:
            usage = db.usage_get(context, id)
        except :
            raise webob.exc.HTTPNotFound(explanation="Usage not found")
 
        usages["usage"] = usage 
        return usages 
 
    def update(self, req):
        usages = {}
        context = req.environ['nova.context']
        authorize(context)
 
        # real logic for update object
        return usages 
 
    def delete(self, req, id):
        return webob.Response(status_int=202)
    
# extension declaration 
class Usages(extensions.ExtensionDescriptor):  
    """Usage Extension Descriptor implementation"""
 
    name = "usages"
    alias = "thkcld-usages"
    namespace = "http://www.thinkcloud.com/ext/api/v1.0/thkcld-usages"
    updated = "2013-11-25T00:00:00+00:00"
 
    def get_resources(self):
        """register the new Usages Restful resource"""
 
        resources = [extensions.ResourceExtension(self.alias,
                 UsagesController())
                 ]
 
        return resources
