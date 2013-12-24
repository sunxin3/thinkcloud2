

#[[file:$NOVA_ROOT$/nova/db/api.py;action:weave]]

#[[section1:start]]

def physical_server_get(context,server_id):
    """Get a physical server or raise if it doesn't exist"""
    return IMPL.physical_server_get(context,server_id)

def physical_server_get_all(context):
    """Get a physical server or raise if it doesn't exist"""
    return IMPL.physical_server_get_all(context)

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
#[[section1:end]]
