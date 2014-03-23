# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
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

from django.views.generic import TemplateView

from openstack_dashboard import usage


class ProjectOverview(usage.UsageView):
    table_class = usage.TenantUsageTable
    usage_class = usage.TenantUsage
    template_name = 'project/overview/usage.html'

    def get_data(self):
        super(ProjectOverview, self).get_data()
        return self.usage.get_instances()
   
    def get_context_data(self, **kwargs):
        context = super(ProjectOverview, self).get_context_data(**kwargs)
        svr_usage = {'lvcc':21, 'lvdi':24, 'hpc':34, 'openstack':40, 'lestor':30, 'test':55, 'demo':53, 'hadoop':10 }
        vm_sys = {'rhel6_4':41, 'centos6_4':54, 'windows7':39, 'windows2008':50 }
        vm_power = {'poweroff':11, 'poweron':184 }
        svr_power = {'poweroff':2, 'poweron':203 }
        context['svr_usage'] = svr_usage
        context['vm_sys'] = vm_sys
        context['vm_power'] = vm_power
        context['svr_power'] = svr_power
        return context

class WarningView(TemplateView):
    template_name = "project/_warning.html"
