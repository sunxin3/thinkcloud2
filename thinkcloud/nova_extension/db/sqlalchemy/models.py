

#[[file:$NOVA_ROOT$/nova/db/sqlalchemy/models.py;action:weave]]

#[[section1:start]]


class PhysicalServer(BASE,NovaBase):
    """ Represents physical server of customized extension"""
    
    __tablename__ = 'thkcld_physical_servers'
    
    id = Column(Integer,primary_key=True,nullable=False, autoincrement=True)
    server_models_id = Column(Integer, ForeignKey('thkcld_server_models.id'),
                       nullable=False)
    is_public = Column(Boolean())
    locked_by = Column(Integer)
    power_states_id = Column(Integer, ForeignKey('thkcld_power_states.id'),
                       nullable=False)
    nc_number = Column(String(64))
    name = Column(String(64))
    description = Column(String(255))
    ipmi_address = Column(String(255))
    cpu_fre    = Column(Float())
    cpu_core_num   = Column(Integer)
    cpu_desc   = Column(String(255))
    mem_total  = Column(Integer)
    mem_desc  = Column(String(255))
    disk_num  = Column(Integer)
    disk_desc = Column(String(255))
    nic_num   = Column(Integer)
    nic_desc  = Column(String(255))
    hba_attached = Column(Boolean())
    hba_port_num  = Column(Integer)
    cpu_socket_num = Column(Integer)
    disk_total     = Column(Integer)
    raid_internal  = Column(String(64))
    raid_external  = Column(String(64))
    
    #build relationships
    rel_model= relationship("ServerModel",order_by="ServerModel.id", 
                        backref="physical_servers"   )
    rel_power_state = relationship("PowerState", order_by="PowerState.id", 
                               backref="physical_servers" 
                                 )
    
    
class ServerModel (BASE,NovaBase):
    """ Represents physical server model of customized extension"""
    __tablename__ = 'thkcld_server_models'
    
    id = Column(Integer,primary_key=True,nullable=False, autoincrement=True)
    
    name = Column(String(64))
    
class PowerState (BASE,NovaBase):
    """ Represents physical power status of customized extension"""
    __tablename__ = 'thkcld_power_states'
    
    id = Column(Integer,primary_key=True,nullable=False, autoincrement=True)
    
    state = Column(String(64))

 
class ChargeRegion(BASE,NovaBase):
    """Represents regions."""

    __tablename__ = 'thkcld_charge_regions'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    name = Column(String(255), nullable=False)


class ChargeItem(BASE,NovaBase):
    """Represents items."""

    __tablename__ = 'thkcld_charge_items'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    name = Column(String(255), nullable=False)


class ChargeItemType(BASE,NovaBase):
    """Represents item types."""

    __tablename__ = 'thkcld_charge_item_types'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    name = Column(String(255), nullable=False)


class ChargePaymentType(BASE,NovaBase):
    """Represents payment types."""

    __tablename__ = 'thkcld_charge_payment_types'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    name = Column(String(255), nullable=False)

    interval_unit = Column(String(255), nullable=False)

    interval_size = Column(Integer, nullable=False)

    is_prepaid = Column(Boolean, nullable=False, default=False)


class ChargeProduct(BASE,NovaBase):
    """Represents products."""

    __tablename__ = 'thkcld_charge_products'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    region_id = Column(Integer,
                       ForeignKey(ChargeRegion.id),
                       nullable=False)
 
    region = relationship(ChargeRegion,
                          backref=backref('thkcld_charge_products'),
                          foreign_keys=region_id,
                          primaryjoin='and_('
                                      'ChargeProduct.region_id == ChargeRegion.id,'
                                      'ChargeProduct.deleted == False)')

    item_id = Column(Integer,
                     ForeignKey(ChargeItem.id),
                     nullable=False)

    item = relationship(ChargeItem,
                        backref=backref('thkcld_charge_products'),
                        foreign_keys=item_id,
                        primaryjoin='and_('
                                    'ChargeProduct.item_id == ChargeItem.id,'
                                    'ChargeProduct.deleted == False)')
 
    item_type_id = Column(Integer,
                          ForeignKey(ChargeItemType.id),
                          nullable=False)

    item_type = relationship(ChargeItemType,
                             backref=backref('thkcld_charge_products'),
                             foreign_keys=item_type_id,
                             primaryjoin='and_('
                                         'ChargeProduct.item_type_id == ChargeItemType.id,'
                                         'ChargeProduct.deleted == False)')

    payment_type_id = Column(Integer,
                             ForeignKey(ChargePaymentType.id),
                             nullable=False)

    payment_type = relationship(ChargePaymentType,
                                backref=backref('thkcld_charge_products'),
                                foreign_keys=payment_type_id,
                                primaryjoin='and_('
                                            'ChargeProduct.payment_type_id == '
                                            'ChargePaymentType.id,'
                                            'ChargeProduct.deleted == False)')

    order_unit = Column(String(255), nullable=False)

    order_size = Column(Integer, nullable=False)

    price = Column(Float, nullable=False)

    currency = Column(String(255), nullable=False)


class ChargeSubscription(BASE,NovaBase):
    """Represents subscriptions."""

    __tablename__ = 'thkcld_charge_subscriptions'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    project_id = Column(Integer, nullable=False, index=True)

    product_id = Column(Integer,
                        ForeignKey(ChargeProduct.id),
                        nullable=False)

    product = relationship(ChargeProduct,
                           backref=backref('thkcld_charge_subscriptions'),
                           foreign_keys=product_id,
                           primaryjoin='and_('
                                       'ChargeSubscription.product_id == ChargeProduct.id,'
                                       'ChargeSubscription.deleted == False)')

    resource_uuid = Column(String(255), nullable=False, index=True)

    resource_name = Column(String(255), nullable=False)

    expires_at = Column(DateTime, nullable=False, index=True)

    status = Column(String(255), nullable=False)


class ChargePurchase(BASE,NovaBase):
    """Represents purchases."""

    __tablename__ = 'thkcld_charge_purchases'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    subscription_id = Column(Integer,
                             ForeignKey(ChargeSubscription.id),
                             nullable=False)

    quantity = Column(BigInteger, nullable=False)

    line_total = Column(Float, nullable=False)

#[[section1:end]]
