

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
    power_states_id = Column(Integer, ForeignKey('thkcld_power_stats.id'),
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
#[[section1:end]]