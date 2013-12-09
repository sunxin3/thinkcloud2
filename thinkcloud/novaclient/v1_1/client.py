

#[[file:$NOVA_CLIENT_ROOT$/novaclient/v1_1/client.py;action:weave]]


#[[section1:start]]

from novaclient.v1_1.contrib import physical_servers
from novaclient.v1_1.contrib import server_models
#[[section1:end]]

#[[section2:start]]
       
        self.physical_servers = physical_servers.Physical_ServerManager(self)
        self.server_models = server_models.Server_ModelManager(self)  
#[[section2:end]]
