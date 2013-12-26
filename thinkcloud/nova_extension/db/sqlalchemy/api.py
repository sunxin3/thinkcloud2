
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

@require_admin_context    
def physical_server_get_all(context):
        server_list = []
        session = get_session()
        resultset = session.query(models.PhysicalServer).all()
        for row in resultset:
            row['state'] = row.power_state.state
            server_list.append(row)
        return server_list;    

    
@require_admin_context    
def server_model_get(context,model_id):
    session = get_session()
    with session.begin():
        query = model_query(context,models.ServerModel,session=session,
                            read_deleted="yes").filter_by(id=model_id)
        result = query.first()
        
        if not result or not query:
            raise  Exception()
        
        return result
    
@require_admin_context    
def server_model_get_all(context):
        query = model_query(context, models.ServerModel)
        return query.all();    
      
@require_admin_context        
def server_model_create(context, values):
    server_model = models.ServerModel()
    server_model.update(values)
    server_model.save()
    return server_model    

@require_admin_context        
def server_model_delete(context, model_id):
    result = model_query(context, models.ServerModel).\
             filter_by(id=model_id).\
             soft_delete()

    return result

@require_admin_context    
def power_state_get(context,power_state_id):
    session = get_session()
    with session.begin():
        query = model_query(context,models.PowerState,session=session,
                            read_deleted="yes").filter_by(id=power_state_id)
        result = query.first()
        
        if not result or not query:
            raise  Exception()
        
        return result        
    
@require_admin_context
def charge_region_get(context, region_id):
    session = get_session()
    with session.begin():
	query = model_query(context,models.ChargeRegion,session=session).filter_by(id=region_id)
        result = query.first()
    if not result or not query:
        raise Exception()

    return result

@require_admin_context
def charge_region_create(context, values):
    charge_region = models.ChargeRegion()
    charge_region.update(values)
    charge_region.save()
    return charge_region

@require_admin_context
def charge_region_delete(context, region_id):
    result = model_query(context, models.ChargeRegion).\
             filter_by(id=region_id).\
             soft_delete()

    return result

@require_admin_context
def charge_region_get_all(context):
    query = model_query(context, models.ChargeRegion)
    return query.all();

@require_admin_context
def charge_item_get(context, item_id):
    session = get_session()
    with session.begin():
        query = model_query(context,models.ChargeItem,session=session).filter_by(id=item_id)
        result = query.first()
    if not result or not query:
        raise Exception()

    return result

@require_admin_context
def charge_item_create(context, values):
    charge_item = models.ChargeItem()
    charge_item.update(values)
    charge_item.save()
    return charge_item

@require_admin_context
def charge_item_delete(context, item_id):
    result = model_query(context, models.ChargeItem).\
             filter_by(id=item_id).\
             soft_delete()

    return result

@require_admin_context
def charge_item_get_all(context):
    query = model_query(context, models.ChargeItem)
    return query.all();
#[[section1:end]]  
