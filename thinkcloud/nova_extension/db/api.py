

#[[file:$NOVA_ROOT$/nova/db/api.py;action:weave]]

#[[section1:start]]

def physical_server_get(context,server_id):
    """Get a physical server or raise if it doesn't exist"""
    return IMPL.physical_server_get(context,server_id)

def physical_server_get_all(context):
    """Get a physical server or raise if it doesn't exist"""
    return IMPL.physical_server_get_all(context)

def physical_server_update(context,server_id,values):
    """Update a physical server """
    return IMPL.physical_server_update(context,server_id,values)

def physical_server_delete(context,server_id):
    """Delete a server model """
    return IMPL.physical_server_delete(context,server_id)

def server_model_get(context,model_id):
    """Get a server model or raise if it doesn't exist"""
    return IMPL.server_model_get(context,model_id)

def server_model_get_all(context):
    """Get all server model """
    return IMPL.server_model_get_all(context)

def server_model_create(context,values):
    """Create a server model """
    return IMPL.server_model_create(context,values)

def server_model_delete(context,model_id):
    """Delete a server model """
    return IMPL.server_model_delete(context,model_id)

def ram_get(context,ram_id):
    """Get a server RAM or raise if it doesn't exist"""
    return IMPL.ram_get(context,ram_id)

def ram_get_all(context):
    """Get all  RAM """
    return IMPL.ram_get_all(context)

def ram_create(context,values):
    """Create RAM """
    return IMPL.ram_create(context,values)

def ram_delete(context,ram_id):
    """Delete a RAM """
    return IMPL.ram_delete(context,ram_id)

def disk_get(context,disk_id):
    """Get a server disk or raise if it doesn't exist"""
    return IMPL.disk_get(context,disk_id)

def disk_get_all(context):
    """Get all  DISK """
    return IMPL.disk_get_all(context)

def disk_create(context,values):
    """Create disk """
    return IMPL.disk_create(context,values)

def disk_delete(context,disk_id):
    """Delete a disk """
    return IMPL.disk_delete(context,disk_id)

def nic_get(context,nic_id):
    """Get a server NIC or raise if it doesn't exist"""
    return IMPL.disk_get(context,nic_id)

def nic_get_all(context):
    """Get all  nic """
    return IMPL.nic_get_all(context)

def nic_create(context,values):
    """Create nic """
    return IMPL.nic_create(context,values)

def nic_delete(context,nic_id):
    """Delete a nic """
    return IMPL.nic_delete(context,nic_id)


def hba_type_get(context,hba_type_id):
    """Get a server hba_type or raise if it doesn't exist"""
    return IMPL.disk_get(context,hba_type_id)

def hba_type_get_all(context):
    """Get all  hba_type """
    return IMPL.hba_type_get_all(context)

def hba_type_create(context,values):
    """Create hba_type """
    return IMPL.hba_type_create(context,values)

def hba_type_delete(context,hba_type_id):
    """Delete a hba_type """
    return IMPL.hba_type_delete(context,hba_type_id)

def hba_get(context,hba_id):
    """Get a server hba or raise if it doesn't exist"""
    return IMPL.disk_get(context,hba_id)

def hba_get_all(context):
    """Get all  hba """
    return IMPL.hba_get_all(context)

def hba_create(context,values):
    """Create hba """
    return IMPL.hba_create(context,values)

def hba_delete(context,hba_id):
    """Delete a hba """
    return IMPL.hba_delete(context,hba_id)

def usage_get(context,usage_id):
    """Get a the usage of the server or raise if it doesn't exist"""
    return IMPL.usage_get(context,usage_id)

def usage_get_all(context):
    """Get all  usage """
    return IMPL.usage_get_all(context)

def usage_create(context,values):
    """Create new usage entry """
    return IMPL.usage_create(context,values)

def usage_delete(context,usage_id):
    """Delete an usage entry """
    return IMPL.usage_delete(context,usage_id)


def power_state_get(context,power_state_id):
    """Get a server model or raise if it doesn't exist"""
    return IMPL.power_state_get(context,power_state_id)

def charge_region_get(context,region_id):
    """Get a charge region or raise if it doesn't exist"""
    return IMPL.charge_region_get(context,region_id)

def charge_region_create(context,values):
    """Create a charge region """
    return IMPL.charge_region_create(context,values)

def charge_region_get_all(context):
    """Get all charge region"""
    return IMPL.charge_region_get_all(context)

def charge_region_delete(context,region_id):
    """Delete a charge region"""
    return IMPL.charge_region_delete(context, region_id)

def charge_item_get(context,item_id):
    """Get a charge item or raise if it doesn't exist"""
    return IMPL.charge_item_get(context,item_id)

def charge_item_create(context,values):
    """Create a charge item """
    return IMPL.charge_item_create(context,values)

def charge_item_get_all(context):
    """Get all charge item"""
    return IMPL.charge_item_get_all(context)

def charge_item_delete(context,item_id):
    """Delete a charge item"""
    return IMPL.charge_item_delete(context, item_id)

def charge_item_type_get(context,item_type_id):
    """Get a charge item type or raise if it doesn't exist"""
    return IMPL.charge_item_type_get(context,item_type_id)

def charge_item_type_create(context,values):
    """Create a charge item type"""
    return IMPL.charge_item_type_create(context,values)

def charge_item_type_get_all(context):
    """Get all charge item type"""
    return IMPL.charge_item_type_get_all(context)

def charge_item_type_delete(context,item_type_id):
    """Delete a charge item type"""
    return IMPL.charge_item_type_delete(context, item_type_id)

def charge_payment_type_get(context,payment_type_id):
    """Get a charge payment type or raise if it doesn't exist"""
    return IMPL.charge_payment_type_get(context,payment_type_id)

def charge_payment_type_create(context,values):
    """Create a charge payment type"""
    return IMPL.charge_payment_type_create(context,values)

def charge_payment_type_get_all(context):
    """Get all charge payment type"""
    return IMPL.charge_payment_type_get_all(context)

def charge_payment_type_delete(context,payment_type_id):
    """Delete a charge payment type"""
    return IMPL.charge_payment_type_delete(context, payment_type_id)

def charge_product_get(context,product_id):
    """Get a charge product or raise if it doesn't exist"""
    return IMPL.charge_product_get(context,product_id)

def charge_product_create(context,values):
    """Create a charge product"""
    return IMPL.charge_product_create(context,values)

def charge_product_get_all(context):
    """Get all charge product"""
    return IMPL.charge_product_get_all(context)

def charge_product_delete(context,product_id):
    """Delete a charge product"""
    return IMPL.charge_product_delete(context, product_id)

def charge_subscription_get(context,subscription_id):
    """Get a charge subscription or raise if it doesn't exist"""
    return IMPL.charge_subscription_get(context,subscription_id)

def charge_subscription_create(context,values):
    """Create a charge subscription"""
    return IMPL.charge_subscription_create(context,values)

def charge_subscription_get_all(context):
    """Get all charge subscription"""
    return IMPL.charge_subscription_get_all(context)

def charge_subscription_delete(context,subscription_id):
    """Delete a charge subscription"""
    return IMPL.charge_subscription_delete(context, subscription_id)

def charge_subscription_update(context,subscription_id,values):
    """Update a charge subscription"""
    return IMPL.charge_subscription_update(context, subscription_id, values)

def charge_purchase_get(context,purchase_id):
    """Get a charge purchase or raise if it doesn't exist"""
    return IMPL.charge_purchase_get(context,purchase_id)

def charge_purchase_create(context,values):
    """Create a charge purchase"""
    return IMPL.charge_purchase_create(context,values)

def charge_purchase_get_all(context):
    """Get all charge purchase"""
    return IMPL.charge_purchase_get_all(context)

def charge_purchase_delete(context,purchase_id):
    """Delete a charge purchase"""
    return IMPL.charge_purchase_delete(context, purchase_id)
#[[section1:end]]
