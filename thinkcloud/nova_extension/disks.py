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
#   Extension for disks  
# Author: Dengfeng Mao
# Email:  mdengfeng@gmail.com

#[[file:$NOVA_ROOT$/nova/api/openstack/compute/contrib/disks.py;action:copy]]

import webob
from webob import exc

from nova.api.openstack import wsgi
from nova import db
from nova import exception
from nova.api.openstack import extensions

authorize = extensions.extension_authorizer('compute', 'disks')
 
# Controller which would response for the request
class DisksController(wsgi.Controller):
    """the Disk API Controller declearation"""
 
    def index(self, req):
        disks = {}
        context = req.environ['nova.context']
        authorize(context)
             
        # logic for get all records from db
       
        return disks 
 
    def create(self, req):
        disks = {}
        context = req.environ['nova.context']
        authorize(context)
 
        # real logic to create the object
        return disks 
 
    def show(self, req, id):
        disks = {}
        context = req.environ['nova.context']
        authorize(context)
 
        try:
            disk = db.disk_get(context, id)
        except :
            raise webob.exc.HTTPNotFound(explanation="Disk not found")
 
        disks["disk"] = disk 
        return disks 
 
    def update(self, req):
        disks = {}
        context = req.environ['nova.context']
        authorize(context)
 
        # real logic for update object
        return disks 
 
    def delete(self, req, id):
        return webob.Response(status_int=202)
    
# extension declaration 
class Disks(extensions.ExtensionDescriptor):  
    """Disk Extension Descriptor implementation"""
 
    name = "disks"
    alias = "thkcld-disks"
    namespace = "http://www.thinkcloud.com/ext/api/v1.0/thkcld-disks"
    updated = "2013-11-25T00:00:00+00:00"
 
    def get_resources(self):
        """register the new Disks Restful resource"""
 
        resources = [extensions.ResourceExtension(self.alias,
                 DisksController())
                 ]
 
        return resources
