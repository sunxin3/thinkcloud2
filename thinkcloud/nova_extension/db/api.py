

#[[file:$NOVA_ROOT$/nova/db/api.py;action:weave]]

#[[section1:start]]

def physical_server_get(context,server_id):
    """Get a physical server or raise if it doesn't exist"""
    return IMPL.physical_server_get(context,server_id)


def server_model_get(context,model_id):
    """Get a server model or raise if it doesn't exist"""
    return IMPL.server_model_get(context,model_id)

def power_state_get(context,power_state_id):
    """Get a server model or raise if it doesn't exist"""
    return IMPL.power_state_get(context,power_state_id)

#[[section1:end]]

