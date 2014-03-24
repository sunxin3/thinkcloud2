# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 Nebula, Inc.
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

import logging
import types
import subprocess
import time
from collections import defaultdict
from django.utils import datetime_safe

from django.conf import settings
from django.core.urlresolvers import reverse
from django.template import defaultfilters as filters
from django.utils.http import urlencode
from django.utils.translation import ugettext_lazy as _

from horizon import tables
from horizon.utils.memoized import memoized

from openstack_dashboard import api
from horizon.mail import send_mail


LOG = logging.getLogger(__name__)


class DeletePhysicalServer(tables.DeleteAction):
    data_type_singular = _("Physical Server")
    data_type_plural = _("Physical Servers")
    def allowed(self, request, server=None):
        return False

    def delete(self, request, obj_id):
        api.nova.physical_server_delete(request, obj_id)


class AddPhysicalServer(tables.LinkAction):
    name = "create"
    verbose_name = _("Add Physical Server")
    url = "horizon:project:physical_servers:create"
    classes = ("ajax-modal", "btn-create")


class EditPhysicalServer(tables.LinkAction):
    name = "edit"
    verbose_name = _("Edit")
    url = "horizon:project:physical_servers:update"
    classes = ("ajax-modal", "btn-edit")

    def allowed(self, request, image=None):
        if image:
            return image.status in ("active",) and \
                image.owner == request.user.tenant_id
        # We don't have bulk editing, so if there isn't an image that's
        # authorized, don't allow the action. filters
        return False

class RebootPhysicalServer(tables.BatchAction):
    name = "reboot"
    action_present = _("Reboot")
    action_past = _("Scheduled reboot of")
    data_type_singular = _("Physical Server")
    data_type_plural = _("Physical Servers")
    classes = ("btn-danger", "btn-reboot")    

    def allowed(self, request, datum):
        #server = api.nova.physical_server_get(request, obj_id)
        #if server.subscription_id != None and server.subscrib_status == "verified":
        if datum.subscription_id != None and datum.subscrib_status == "verified":
            return True
        return False
    
    def action(self, request, obj_id):
        ipmi_address = api.nova.physical_server_get(request, obj_id).ipmi_address
        reboot_cmd = 'ipmitool -I lan -H ' + ipmi_address + ' -U lenovo -P lenovo chassis power reset'
        p = subprocess.Popen(reboot_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        time.sleep(3)
        p.kill()
	for result in p.stdout.readlines():
	    if result == 'Chassis Power Control: Reset\n':
	    #TODO by sunxin this is a hardcoding, need to modify later
                api.nova.physical_server_update(request, obj_id, power_states_id=2)
		break
    
class ShutdownPhysicalServer(tables.BatchAction):
    name = "shutdown"
    action_present = _("Shutdown")
    action_past = _("Scheduled shutdown of")
    data_type_singular = _("Physical Server")
    data_type_plural = _("Physical Servers")
    classes = ("btn-danger", "btn-reboot")    

    def allowed(self, request, datum):
        #server = api.nova.physical_server_get(request, obj_id)
        #if server.subscription_id != None and server.subscrib_status == "verified":
        if datum.subscription_id != None and datum.subscrib_status == "verified":
            return True
        return False
    
    def action(self, request, obj_id):
        ipmi_address = api.nova.physical_server_get(request, obj_id).ipmi_address
        shutdown_cmd = 'ipmitool -I lan -H ' + ipmi_address + ' -U lenovo -P lenovo chassis power off'
        p = subprocess.Popen(shutdown_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        time.sleep(3)
        p.kill()
	for result in p.stdout.readlines():
            if result == 'Chassis Power Control: Down/Off\n':
                api.nova.physical_server_update(request, obj_id, power_states_id=2)
                break

class PoweronPhysicalServer(tables.BatchAction):
    name = "poweron"
    action_present = _("Power on")
    action_past = _("Scheduled power on of")
    data_type_singular = _("Physical Server")
    data_type_plural = _("Physical Servers")
    classes = ("btn-danger", "btn-reboot")

    def allowed(self, request, datum):
        #server = api.nova.physical_server_get(request, obj_id)
        #if server.subscription_id != None and server.subscrib_status == "verified":
        if datum.subscription_id != None and datum.subscrib_status == "verified":
            return True
        return False

    def action(self, request, obj_id):
        ipmi_address = api.nova.physical_server_get(request, obj_id).ipmi_address
        poweron_cmd = 'ipmitool -I lan -H ' + ipmi_address + ' -U lenovo -P lenovo chassis power on'
        p = subprocess.Popen(poweron_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        time.sleep(3)
        p.kill()
        for result in p.stdout.readlines():
            if result == 'Chassis Power Control: Up/On\n':
                api.nova.physical_server_update(request, obj_id, power_states_id=1)
                break

class PasswordPhysicalServer(tables.BatchAction):
    name = "changepassword"
    action_present = _("Change IPMI Password")
    action_past = _("Scheduled change IPMI password of")
    data_type_singular = _(" ")
    data_type_plural = _(" ")
    classes = ("btn-danger", "btn-reboot")

    def allowed(self, request, datum):
        #server = api.nova.physical_server_get(request, obj_id)
        #if server.subscription_id != None and server.subscrib_status == "verified":
        if datum.subscription_id != None and datum.subscrib_status == "verified":
            return True
        return False

    def action(self, request, obj_id):
        ipmi_address = api.nova.physical_server_get(request, obj_id).ipmi_address
        password_list = '0123456789'
        import random
        import string
        password = string.join(random.sample(password_list, 6), sep='')
        pass_wd_cmd = 'ipmitool -I lan -H ' + ipmi_address + ' -U lenovo -P lenovo user set password 3 ' + password
        p = subprocess.Popen(pass_wd_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        time.sleep(3)
        p.kill()
        api.nova.physical_server_update(request, obj_id, ipmi_password=password)
        '''for result in p.stdout.readlines():
            if result == 'Set session password\n':
            #TODO by sunxin this is a hardcoding, need to modify later
                api.nova.physical_server_update(request, obj_id, ipmi_password=password)
                break'''

class ApplyPhysicalServer(tables.BatchAction):
    name = "apply"
    action_present = _("Apply")
    action_past = _("Scheduled application of")
    data_type_singular = _("Physical Server")
    data_type_plural = _("Physical Servers")
    classes = ("btn-danger", "btn-reboot")
    
    def allowed(self, request, datum):
        #server = api.nova.physical_server_get(request, obj_id)
        if datum.subscription_id == None:
            return True
        return False

    def action(self, request, obj_id):
        now = datetime_safe.datetime.now().isoformat()

        charge_product_id = None
        charge_products = api.nova.charge_product_list(request)
        for charge_product in charge_products:
            if charge_product.item_name == 'physical_server':
		         charge_product_id = charge_product.id

        resource_displayname = api.nova.physical_server_get(request, obj_id).name
        subscription = api.nova.charge_subscription_create(request, status='apply', product_id=charge_product_id,resource_uuid=obj_id,user_id=request.user.id, project_id=request.user.tenant_id, resource_name=resource_displayname, applied_at=now)

        #LOG.debug("test for sunxin %s" % subscription.id)
        api.nova.physical_server_update(request, obj_id, subscription_id=subscription.id)

        #Send people mail
        #applier_mail_perfix = api.keystone.user_get(request, request.user.id,).name
        applier_mail_perfix = request.user.username
        #TODO by sunxin
        applier_mail = applier_mail_perfix + '@lenovo.com'
        
        mail_title = "[Notice] Server Application Issued"
        mail_content = "Our user " + applier_mail + " asked for a server application, Please handle it immediately." 
        send_mail(mail_title, mail_content, applier_mail)

class PublicPhysicalServer(tables.BatchAction):
    name = "public"
    action_present = _("Public")
    action_past = _("Scheduled application of")
    data_type_singular = _("Physical Server")
    data_type_plural = _("Physical Servers")
    classes = ("btn-danger", "btn-reboot")
    
    def allowed(self, request, obj_id):
         return False

    def action(self, request, obj_id):
        now = datetime_safe.datetime.now().isoformat()

        '''charge_product_id = None
        charge_products = api.nova.charge_product_list(request)
        for charge_product in charge_products:
            if charge_product.item_name == 'physical_server':
		         charge_product_id = charge_product.id

        resource_displayname = api.nova.physical_server_get(request, obj_id).name
        subscription = api.nova.charge_subscription_create(request, status='apply', product_id=charge_product_id,resource_uuid=obj_id,user_id=request.user.id, project_id=request.user.tenant_id, resource_name=resource_displayname, applied_at=now)'''

        #LOG.debug("test for sunxin %s" % subscription.id)
        api.nova.physical_server_update(request, obj_id, is_public=1)

        '''#Send people mail
        applier_mail_perfix = api.keystone.user_get(request, request.user.id,).name
        #TODO by sunxin
        applier_mail = applier_mail_perfix + '@lenovo.com'
        
        mail_title = "[Notice] Server Application Issued"
        mail_content = "Our user " + applier_mail + " asked for a server application, Please handle it immediately." 
        send_mail(mail_title, mail_content, applier_mail)'''

class PrivatePhysicalServer(tables.BatchAction):
   name = "private"
   action_present = _("Private")
   action_past = _("Scheduled private of")
   data_type_singular = _("Physical Server")
   data_type_plural = _("Physical Servers")
   classes = ("btn-danger", "btn-reboot")
   
   def allowed(self, request, obj_id):
       return False

   def action(self, request, obj_id):
       '''now = datetime_safe.datetime.now().isoformat()

       charge_product_id = None
       charge_products = api.nova.charge_product_list(request)
       for charge_product in charge_products:
           if charge_product.item_name == 'physical_server':
	         charge_product_id = charge_product.id

       resource_displayname = api.nova.physical_server_get(request, obj_id).name
       subscription = api.nova.charge_subscription_create(request, status='apply', product_id=charge_product_id,resource_uuid=obj_id,user_id=request.user.id, project_id=request.user.tenant_id, resource_name=resource_displayname, applied_at=now)'''

       #LOG.debug("test for sunxin %s" % subscription.id)
       api.nova.physical_server_update(request, obj_id, is_public=0)

       '''#Send people mail
       applier_mail_perfix = api.keystone.user_get(request, request.user.id,).name
       #TODO by sunxin
       applier_mail = applier_mail_perfix + '@lenovo.com'
       
       mail_title = "[Notice] Server Application Issued"
       mail_content = "Our user " + applier_mail + " asked for a server application, Please handle it immediately." 
       send_mail(mail_title, mail_content, applier_mail)'''

def filter_tenants():
    return getattr(settings, 'IMAGES_LIST_FILTER_TENANTS', [])


@memoized
def filter_tenant_ids():
    return map(lambda ft: ft['tenant'], filter_tenants())



class UpdateRow(tables.Row):
    ajax = True

    def get_data(self, request, server_id):
        server = api.nova.physical_server_get(request, server_id)
        return server

    def load_cells(self, server=None):
        super(UpdateRow, self).load_cells(server)
        # Tag the row with the server category for client-side filtering.
        server = self.datum
        my_tenant_id = self.table.request.user.tenant_id
        server_categories = get_server_categories(server, my_tenant_id)
        for category in server_categories:
            self.classes.append('category-' + category)
      
class OwnerFilter(tables.FixedFilterAction):
    def get_fixed_buttons(self):
        def make_dict(text, tenant, icon):
            return dict(text=text, value=tenant, icon=icon)
        buttons = [make_dict('Reserved by Me', 'reserved', 'icon-star')]
        buttons.append(make_dict('Free Available', 'free', 'icon-home'))
      
        return buttons

    def categorize(self, table, servers):
        user_tenant_id = table.request.user.tenant_id
        tenants = defaultdict(list)
        for server in servers:
            categories = get_server_categories(server,user_tenant_id)
            for category in categories:
                if category == "free":
                    server.ipmi_address = "N/A"
                    server.ipmi_password = "N/A"
		if category == "reserved":
		    if server.subscrib_status != "verified":
                        server.ipmi_address = "N/A"
                        server.ipmi_password = "N/A"
                tenants[category].append(server)
        return tenants
    
def get_server_categories(server,user_tenant_id):
    categories = []
    if server.is_public: 
        if server.subscription_id == None:
            categories.append('free')
        elif server.subscrib_project_id == user_tenant_id:
            categories.append('reserved')
    else:
        if server.subscription_id == None: 
            categories.append('private_free')
        else:
            categories.append('private_reserved')
    return categories

def  total_memory(server):
    return _("%sGB") % server.ram_sum

def  total_disk(server):
    return _("%sT") % server.disk_sum




class PhysicalserversTable(tables.DataTable):

    name = tables.Column("name",
                         link=("horizon:project:physical_servers:"
                               "detail"),
                         verbose_name=_("Server Name"))
    nc_num = tables.Column("nc_number",
                             verbose_name=_("NC Number"))
    model = tables.Column("model",
                               verbose_name=_("Model"),
                               filters=(filters.upper,))
    status = tables.Column("state",
                           filters=(filters.title,),
                           verbose_name=_("Power State"),)
    ipmi  = tables.Column("ipmi_address",
                          verbose_name= _("IPMI Address"))
    ipmi_password  = tables.Column("ipmi_password",
                          verbose_name= _("IPMI Password"))
    public = tables.Column("is_public",
                           verbose_name=_("Public"),
                           empty_value=False,
                           filters=(filters.yesno, filters.capfirst))
    cpu = tables.Column("cpu_desc", verbose_name=_("CPU"))
    
    memory = tables.Column(total_memory, verbose_name=_("Memory"))
    
    storage = tables.Column(total_disk, verbose_name=_("Storage"))
    
    nics    = tables.Column("nic_sum", verbose_name=_("Nics"),
                            filters=(filters.linebreaksbr,))
    subscrib_status = tables.Column("subscrib_status", verbose_name=_("Subscrib Status"))

    def get_object_id(self, datum):
        if type(datum.id) == types.IntType:
            return unicode(str(datum.id))
        return datum.id

    class Meta:
        name = "physicalservers"
        row_class = UpdateRow
        verbose_name = _("Physical Servers")
        # Hide the image_type column. Done this way so subclasses still get
        # all the columns by default.
        columns = ["nc_num", "model", "name", "cpu","memory","storage","nics","status","ipmi", "ipmi_password", "subscrib_status"]
        table_actions = (OwnerFilter,)
        row_actions = (ApplyPhysicalServer,RebootPhysicalServer,ShutdownPhysicalServer,PoweronPhysicalServer,PasswordPhysicalServer)
