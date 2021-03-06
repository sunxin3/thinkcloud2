

#[[file:$NOVA_CLIENT_ROOT$/novaclient/v1_1/client.py;action:weave]]


#[[section1:start]]

from novaclient.v1_1.contrib import physical_servers
from novaclient.v1_1.contrib import server_models
from novaclient.v1_1.contrib import charge_regions
from novaclient.v1_1.contrib import charge_items
from novaclient.v1_1.contrib import charge_item_types
from novaclient.v1_1.contrib import charge_payment_types
from novaclient.v1_1.contrib import charge_products
from novaclient.v1_1.contrib import charge_subscriptions
from novaclient.v1_1.contrib import charge_purchases
#[[section1:end]]

#[[section2:start]]
       
        self.physical_servers = physical_servers.Physical_ServerManager(self)
        self.server_models = server_models.Server_ModelManager(self)  
        self.charge_regions = charge_regions.Charge_RegionManager(self)  
        self.charge_items = charge_items.Charge_ItemManager(self)  
        self.charge_item_types = charge_item_types.Charge_Item_typeManager(self)  
        self.charge_payment_types = charge_payment_types.Charge_Payment_typeManager(self)  
        self.charge_products = charge_products.Charge_ProductManager(self)  
        self.charge_subscriptions = charge_subscriptions.Charge_SubscriptionManager(self)  
        self.charge_purchases = charge_purchases.Charge_PurchaseManager(self)  
#[[section2:end]]
