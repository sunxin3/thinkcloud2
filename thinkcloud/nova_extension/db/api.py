

#[[file:$NOVA_ROOT$/nova/db/api.py;action:weave]]

#[[section1:start]]

def physical_server_get(context,server_id):
    """Get a document or raise if it doesn't exist"""
    return IMPL.physical_server_get(context,server_id)



#[[section1:end]]

