# How to develop nova extension
   The following steps describe how to develop a nova extension.
 
 1. Add extension source files
   All nova extension files should be placed into the following folder:
     <os_root>/nova/nova/api/openstack/compute/contrib
   The following is an example of extension:
```python
   #---------------------------------------------------------------------------
   # Exaple codes for extension
   #---------------------------------------------------------------------------
    import webob
    from webob import exc

    from nova.api.openstack import wsgi
    from nova import db
    from nova import exception
    from nova.api.openstack import extensions

    authorize = extensions.extension_authorizer('compute', 'physical_servers')
 
    # Controller which would response for the request
    class Physical_serversController(wsgi.Controller):
       """the Physical_server API Controller declearation"""
 
    def index(self, req):
        import pdb; pdb.set_trace()
        physical_servers = {}
        context = req.environ['nova.context']
        authorize(context)
             
        # logic for get all records from db
       
        return physical_servers 
 
    def create(self, req):
        physical_servers = {}
        context = req.environ['nova.context']
        authorize(context)
 
        # real logic to create the object
        return physical_servers 
 
    def show(self, req, id):
        physical_servers = {}
        context = req.environ['nova.context']
        authorize(context)
 
        try:
            physical_server = db.physical_server_get(context, id)
        except  Exception:
            raise webob.exc.HTTPNotFound(explanation="Physical_server not found")
        
 
        physical_servers["physical_server"] = physical_server 
        return physical_servers 
 
    def update(self, req):
        physical_servers = {}
        context = req.environ['nova.context']
        authorize(context)
 
        # real logic for update object
        return physical_servers 
 
    def delete(self, req, id):
        return webob.Response(status_int=202)
    
    # extension declaration 
    class Physical_servers(extensions.ExtensionDescriptor):  
        """Physical_server ExtensionDescriptor implementation"""
 
    name = "physical_servers"
    alias = "thkcld-physical_servers"
    namespace = "http://www.thinkcloud.com/ext/api/v1.0/thkcld-physical_servers"
    updated = "2013-11-25T00:00:00+00:00"
 
    def get_resources(self):
        """register the new Physical_servers Restful resource"""
 
        resources = [extensions.ResourceExtension(self.alias,
                 Physical_serversController())
                 ]
 
        return resources
    #---------------------------------------------------------------------------
    #  Example End
    #---------------------------------------------------------------------------
```
 **Tips:**
 * There is name convention strict in the nova extension.
 ** The extension file name should be all lower case. The class name for 
 registry the extension should have the same name But the first character is 
 upper case 
 ** The extension should have two classes. One is Controller which would reponse
 for the request. The other one is to registry the extension.
 
 After the extension was added correrctly. You can get the extension name by
 the following command
 ```shell
     curl -X GET -H 'X-Auth-Token:8a2bcd2f218a42fe8cb3ce94516b4afa' http://192.168.110.90:8774/v2/dc9238e0d0a046cd80ecc4b744da5878/extensions
 ```
 
 2. In the extension controller, it would get data from database. By the step 1
 We just get an extension which can response the URL, But it can't fetch any 
 data until we make the database be ready.
 The nova extension use sqlalchemy ORM framework.
 * 1. Add an abstract interace to  <OS_ROOT>/nova/db/api.py
 ```python
    def physical_server_get(context,server_id):
    """Get a physical server or raise if it doesn't exist"""
    return IMPL.physical_server_get(context,server_id)
 ```
 
 * 2. Above interface would be implemented by the sqlalchemy api. The file
 location is <OS_ROOT>/nova/db/sqlalchemy/api.py
 
 ```python         
 
    @require_admin_context
    def physical_server_get(context,server_id):
    session = get_session()
    with session.begin():
 
        query = model_query(context,models.PhysicalServer,session=session,
                            read_deleted="yes").filter_by(id=server_id)
        result = query.first()
        
        if not result or not query:
            raise  Exception()
        
        return result   
```

3. The sqlalchemy api would do all query work. But it denpends on the data
model definiton in which the database table was mapped to python class. So to 
make above api work, we should add new data model defniton into
<OS_ROOT>/nova/db/sqlalchemy/models.py

```python
    class PhysicalServer(BASE,NovaBase):
    """ Represents physical server of customized extension"""
    
    __tablename__ = 'thkcld_physical_servers'
    
    id = Column(Integer,primary_key=True,nullable=False, autoincrement=True)
    server_model_id = Column(Integer, ForeignKey('thkcld_server_models.id'),
                       nullable=False)
    is_public = Column(Boolean())
    locked_by = Column(Integer, ForeignKey('thkcld_server_apply.id'))
    power_state_id = Column(Integer, ForeignKey('thkcld_power_stats.id'),
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
```

Then the new extension is ready to work.
We can test the extesnion by the curl like this:
```shell
    http://192.168.110.90:8774/v2/dc9238e0d0a046cd80ecc4b744da5878/thkcld-physical_servers/1
 
```

#How to add commands to nova client
  After the nova extension is ready, we are going to add commands to nova clien.
which would call nova extension to fetch data from database.
1. Add interface to interact with nova extension. The file should be placed into
<pyhon-novaclien>/novaclient/v1_1
```python
    # Copyright 2013
    """
    physical server interface.
    """
   from novaclient import base
   from novaclient import exceptions
   from novaclient import utils
   from novaclient.openstack.common.py3kcompat import urlutils


    class PhysicalServers(base.Resource):


    def __repr__(self):
        return "<PhysicalServer: %s>" % self.name

   

    @property
    def is_public(self):
        """
        Provide a user-friendly accessor to os-flavor-access:is_public
        """
        return self._info.get("os-flavor-access:is_public", 'N/A')

    

    def delete(self):
        """
        Delete this flavor.
        """
        self.manager.delete(self)


    class PhysicalServersManager(base.ManagerWithFind):
        """
        Manage :class:`Flavor` resources.
        """
        resource_class = PhysicalServers
        is_alphanum_id_allowed = True

    def list(self, detailed=True, is_public=True):
        """
        Get a list of all physical servers.

        :rtype: list of :class:`PhysicalServer`.
        """
        qparams = {}
        # is_public is ternary - None means give all flavors.
        # By default Nova assumes True and gives admins public flavors
        # and flavors from their own projects only.
        if not is_public:
            qparams['is_public'] = is_public
        query_string = "?%s" % urlutils.urlencode(qparams) if qparams else ""

        detail = ""
        if detailed:
            detail = "/detail"

        return self._list("/thkcld-physical_servers%s%s" % (detail, query_string), "physical_server")

    def get(self, physical_server_id):
        """
        Get a specific physical_server.

        :param flavor: The ID of the :class:`PhysicalServer` to get.
        :rtype: :class:`PhyscialServer`
        """
        
        return self._get("/thkcld-physical_servers/%s" % physical_server_id, "physical_server")

    def delete(self, physical_server):
        """
        Delete a specific physical_server.

        :param physical_server: The ID of the :class:`PhysicalServer` to get.
        :param purge: Whether to purge record from the database
        """
        self._delete("/thkcld-physical_servers/%s" % base.getid(physical_server))

    def create(self, user_id, server_model_Id, locked_by, power_state_id,name,
               description, is_public=True):
        """
        Create (allocate) a  floating ip for a tenant

        :param name: Descriptive name of the flavor
        :param ram: Memory in MB for the flavor
        :param vcpu: Number of VCPUs for the flavor
        :param disk: Size of local disk in GB
        :param flavorid: ID for the flavor (optional). You can use the reserved
                         value ``"auto"`` to have Nova generate a UUID for the
                         flavor in cases where you cannot simply pass ``None``.
        :param swap: Swap space in MB
        :param rxtx_factor: RX/TX factor
        :rtype: :class:`Flavor`
        """

        body = {
            "physical_server": {
                "user_id": user_id,
                "server_model_id": server_model_id,
                "locked_by": locked_by,
                "power_state_id": power_state_id,
                "name": name,
                "description": description,
                "is_public": is_public,
            }
        }

        return self._create("/thkcld_physical_servers", body, "physical_server")
    
```

2. Regist above interface into client. Add the following statements into
<python-novaclient>/novaclien/v1_1/client.py
```python
    #import the interface package
    from novaclient.v1_1 import physical_servers
 ```

Initialize the interface in "__init__" in  <python-novaclient>/novaclien/v1_1/client.py

```python
    self.physical_servers = physical_servers.PhysicalServersManager(self)
```

3.Add an entry to <python-novaclient>/novaclien/v1_1/shell.py. Then nova client
command can be mapped to the python function

```python
    def _print_physical_server(physical_server):

        info = physical_server._info.copy()
        utils.print_dict(info)
    
    def _find_physical_server(cs,physical_server):
    """Get an physical server by name or ID."""
    return utils.find_resource(cs.physical_servers, physical_server)
    
    
    
    @utils.arg('physical_server', metavar='<physical_server>', 
           help='Name or ID of physical_server.')
    def do_physical_server_show(cs, args):
    """Show details about the given physical_server."""
    physical_server = _find_physical_server(cs, args.physical_server)
    _print_physical_server(physical_server)

```

**Tips**
  There is a name convension when mapping the command line to the python
action. e.g.
```shell
    nova physical-server-show 1
```
The command "physical-server-show" would be mapped to "do_physical_server_show"

That's all. If all are right. Then you try the command:
```shell
   nova physical-server-show 1 
```
you should get the output like this:
```shell
+-----------------+---------------------------------------------------------------------+
| Property        | Value                                                               |
+-----------------+---------------------------------------------------------------------+
| cpu_core_num    | None                                                                |
| cpu_desc        | None                                                                |
| cpu_fre         | 3.5                                                                 |
| cpu_socket_num  | None                                                                |
| created_at      | 2013-11-27T00:00:00.000000                                          |
| deleted         | None                                                                |
| deleted_at      | None                                                                |
| description     | 1 x Intel? Ci3-4330 processor 3.5 GHz, 2C, 4M Cache, 1.00 GT/s, 65W |
| disk_desc       | 1 x 500 GB 7200 RPM 3.5" DC SATA                                    |
| disk_num        | None                                                                |
| disk_total      | None                                                                |
| hba_attached    | None                                                                |
| hba_port_num    | None                                                                |
| id              | 1                                                                   |
| ipmi_address    | None                                                                |
| is_public       | True                                                                |
| locked_by       | None                                                                |
| mem_desc        | 4 GB (1 x 4 GB PC3-12800E 1600MHz DDR3 ECC-UD                       |
| mem_total       | 4                                                                   |
| name            | Test Server1                                                        |
| nc_number       | None                                                                |
| nic_desc        | None                                                                |
| nic_num         | None                                                                |
| power_state_id  | 1                                                                   |
| raid_external   | None                                                                |
| raid_internal   | None                                                                |
| server_model_id | 1                                                                   |
| updated_at      | None                                                                |
+-----------------+---------------------------------------------------------------------+
    
```