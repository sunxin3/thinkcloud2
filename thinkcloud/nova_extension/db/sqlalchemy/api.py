
#[[file:$NOVA_ROOT$/nova/db/sqlalchemy/api.py;action:weave]]

#[[section1:start]]
@require_admin_context
def physical_server_get(context,server_id):
    session = get_session()
    with session.begin():
        #query = model_query(context,models.PhysicalServer,session=session,read_deleted="yes")
        query = model_query(context,models.PhysicalServer,session=session,
                            read_deleted="yes").filter_by(id=server_id)
        result = query.first()
        
        if not result or not query:
            raise  Exception()
        
        return result 
    
#[[section1:end]]  