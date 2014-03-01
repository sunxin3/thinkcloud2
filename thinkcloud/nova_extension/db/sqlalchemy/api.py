
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
        
        result['model'] = result.rel_model.name
        return result 

@require_admin_context    
def physical_server_get_all(context):
        server_list = []
        session = get_session()
        query = model_query(context,models.PhysicalServer,session=session,
                            read_deleted="no");
        resultset = query.all()
        for row in resultset:
            row['state'] = row.rel_power_state.state
            row['model'] = row.rel_model.name
            # get RAMs of server
            ram_ids = []
            row['ram_sum'] = 0
            for ram_item in row.rel_ram:
                ram_ids.append(ram_item.id)
                row['ram_sum'] = row['ram_sum'] + ram_item.capacity * ram_item.quantity
            row['ram_ids'] = ','.join(str(v) for v in ram_ids)
           
            
            disk_ids = []
            row['disk_sum'] = 0 
            for  disk_item in row.rel_disk:
                disk_ids.append(disk_item.id)
                row['disk_sum'] = row['disk_sum'] + disk_item.capacity
            row['disk_ids'] = ','.join(str(v) for v in disk_ids)            
            
            nic_ids = []
            row['nic_sum'] = "" 
            for  nic_item in row.rel_nic:
                nic_ids.append(nic_item.id)
                row['nic_sum'] +=  str(nic_item.interface_number) + " X " + str(nic_item.interface) + "G\n"
            row['nic_ids'] = ','.join(str(v) for v in nic_ids)      
                        
            if row.subscription_id != None :
                row['subscrib_project_id'] = row.rel_subscription.project_id         
            
            server_list.append(row)
        return server_list;    

@require_admin_context        
def physical_server_delete(context, server_id):
    result = model_query(context, models.PhysicalServer).\
             filter_by(id=server_id).\
             soft_delete()

    return result

    
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
def ram_get(context,ram_id):
    session = get_session()
    with session.begin():
        query = model_query(context,models.Ram,session=session,
                            read_deleted="yes").filter_by(id=ram_id)
        result = query.first()
        
        if not result or not query:
            raise  Exception()
        
        return result
    
@require_admin_context    
def ram_get_all(context):
        query = model_query(context, models.Ram)
        return query.all();    
      
@require_admin_context        
def ram_create(context, values):
    ram_obj = models.Ram()
    ram_obj.update(values)
    ram_obj.save()
    return ram_obj    

@require_admin_context        
def ram_delete(context, ram_id):
    result = model_query(context, models.Ram).\
             filter_by(id=ram_id).\
             soft_delete()

    return result


@require_admin_context    
def disk_get(context,disk_id):
    session = get_session()
    with session.begin():
        query = model_query(context,models.Disk,session=session,
                            read_deleted="yes").filter_by(id=disk_id)
        result = query.first()
        
        if not result or not query:
            raise  Exception()
        
        return result
    
@require_admin_context    
def disk_get_all(context):
        query = model_query(context, models.Disk)
        return query.all();    
      
@require_admin_context        
def disk_create(context, values):
    disk_obj = models.Disk()
    disk_obj.update(values)
    disk_obj.save()
    return disk_obj    

@require_admin_context        
def disk_delete(context, disk_id):
    result = model_query(context, models.Disk).\
             filter_by(id=disk_id).\
             soft_delete()

    return result


@require_admin_context    
def nic_get(context,nic_id):
    session = get_session()
    with session.begin():
        query = model_query(context,models.Nic,session=session,
                            read_deleted="yes").filter_by(id=nic_id)
        result = query.first()
        
        if not result or not query:
            raise  Exception()
        
        return result
    
@require_admin_context    
def nic_get_all(context):
        query = model_query(context, models.Nic)
        return query.all();    
      
@require_admin_context        
def nic_create(context, values):
    nic_obj = models.Nic()
    nic_obj.update(values)
    nic_obj.save()
    return nic_obj    

@require_admin_context        
def nic_delete(context, nic_id):
    result = model_query(context, models.Nic).\
             filter_by(id=nic_id).\
             soft_delete()

    return result



@require_admin_context    
def hba_type_get(context,hba_type_id):
    session = get_session()
    with session.begin():
        query = model_query(context,models.HbaType,session=session,
                            read_deleted="yes").filter_by(id=hba_type_id)
        result = query.first()
        
        if not result or not query:
            raise  Exception()
        
        return result
    
@require_admin_context    
def hba_type_get_all(context):
        query = model_query(context, models.HbaType)
        return query.all();    
      
@require_admin_context        
def hba_type_create(context, values):
    hba_type_obj = models.HbaType()
    hba_type_obj.update(values)
    hba_type_obj.save()
    return hba_type_obj    

@require_admin_context        
def hba_type_delete(context, hba_type_id):
    result = model_query(context, models.HbaType).\
             filter_by(id=hba_type_id).\
             soft_delete()

    return result


    
@require_admin_context    
def hba_get(context,hba_id):
    session = get_session()
    with session.begin():
        query = model_query(context,models.Hba,session=session,
                            read_deleted="yes").filter_by(id=hba_id)
        result = query.first()
        
        if not result or not query:
            raise  Exception()
        
        return result
    
@require_admin_context    
def hba_get_all(context):
        query = model_query(context, models.Hba)
        return query.all();    
      
@require_admin_context        
def hba_create(context, values):
    hba_obj = models.Hba()
    hba_obj.update(values)
    hba_obj.save()
    return hba_obj    

@require_admin_context        
def hba_delete(context, hba_id):
    result = model_query(context, models.Hba).\
             filter_by(id=hba_id).\
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

@require_admin_context
def charge_item_type_get(context, item_type_id):
    session = get_session()
    with session.begin():
        query = model_query(context,models.ChargeItemType,session=session).filter_by(id=item_type_id)
        result = query.first()
    if not result or not query:
        raise Exception()

    return result

@require_admin_context
def charge_item_type_create(context, values):
    charge_item_type = models.ChargeItemType()
    charge_item_type.update(values)
    charge_item_type.save()
    return charge_item_type

@require_admin_context
def charge_item_type_delete(context, item_type_id):
    result = model_query(context, models.ChargeItemType).\
             filter_by(id=item_type_id).\
             soft_delete()

    return result

@require_admin_context
def charge_item_type_get_all(context):
    query = model_query(context, models.ChargeItemType)
    return query.all();

@require_admin_context
def charge_payment_type_get(context, payment_type_id):
    session = get_session()
    with session.begin():
        query = model_query(context,models.ChargePaymentType,session=session).filter_by(id=payment_type_id)
        result = query.first()
    if not result or not query:
        raise Exception()

    return result

@require_admin_context
def charge_payment_type_create(context, values):
    charge_payment_type = models.ChargePaymentType()
    charge_payment_type.update(values)
    charge_payment_type.save()
    return charge_payment_type

@require_admin_context
def charge_payment_type_delete(context, payment_type_id):
    result = model_query(context, models.ChargePaymentType).\
             filter_by(id=payment_type_id).\
             soft_delete()

    return result

@require_admin_context
def charge_payment_type_get_all(context):
    query = model_query(context, models.ChargePaymentType)
    return query.all();

@require_admin_context
def charge_product_get(context, product_id):
    session = get_session()
    with session.begin():
        query = model_query(context,models.ChargeProduct,session=session).filter_by(id=product_id)
        result = query.first()
    if not result or not query:
        raise Exception()

    return result

@require_admin_context
def charge_product_create(context, values):
    charge_product = models.ChargeProduct()
    charge_product.update(values)
    charge_product.save()
    return charge_product

@require_admin_context
def charge_product_delete(context, product_id):
    result = model_query(context, models.ChargeProduct).\
             filter_by(id=product_id).\
             soft_delete()

    return result

@require_admin_context
def charge_product_get_all(context):
    product_list = []
    session = get_session()
    with session.begin():
	resultset = session.query(models.ChargeProduct).all()
    	for row in resultset:
            row['item_name'] = row.item.name
            row['item_type_name'] = row.item_type.name
            product_list.append(row)
    return product_list;

@require_admin_context
def charge_subscription_get(context, subscription_id):
    session = get_session()
    with session.begin():
        query = model_query(context,models.ChargeSubscription,session=session).filter_by(id=subscription_id)
        result = query.first()
    if not result or not query:
        raise Exception()

    return result

@require_admin_context
def charge_subscription_create(context, values):
    charge_subscription = models.ChargeSubscription()
    charge_subscription.update(values)
    charge_subscription.save()
    return charge_subscription

@require_admin_context
def charge_subscription_delete(context, subscription_id):
    result = model_query(context, models.ChargeSubscription).\
             filter_by(id=subscription_id).\
             soft_delete()

    return result

@require_admin_context
def charge_subscription_update(context, subscription_id, values):
    session = get_session()
    with session.begin():
        subscription_ref = charge_subscription_get(context, subscription_id)
        subscription_ref.update(values)
	subscription_ref.save(session=session)

@require_admin_context
def charge_subscription_get_all(context):
    subscription_list = []
    session = get_session()
    with session.begin():
        resultset = session.query(models.ChargeSubscription).all()
        for row in resultset:
            row['item'] = row.rel_charge_product.item.name
            subscription_list.append(row)
    return subscription_list

@require_admin_context
def charge_purchase_get(context, purchase_id):
    session = get_session()
    with session.begin():
        query = model_query(context,models.ChargePurchase,session=session).filter_by(id=purchase_id)
        result = query.first()
    if not result or not query:
        raise Exception()

    return result

@require_admin_context
def charge_purchase_create(context, values):
    charge_purchase = models.ChargePurchase()
    charge_purchase.update(values)
    charge_purchase.save()
    return charge_purchase

@require_admin_context
def charge_purchase_delete(context, purchase_id):
    result = model_query(context, models.ChargePurchase).\
             filter_by(id=purchase_id).\
             soft_delete()

    return result

@require_admin_context
def charge_purchase_get_all(context):
    query = model_query(context, models.ChargePurchase)
    return query.all()
#[[section1:end]]  
