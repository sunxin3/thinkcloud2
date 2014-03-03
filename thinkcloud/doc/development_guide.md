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
_1. Add an abstract interace to  <OS_ROOT>/nova/db/api.py
 ```python
    def physical_server_get(context,server_id):
    """Get a physical server or raise if it doesn't exist"""
    return IMPL.physical_server_get(context,server_id)
 ```
 
 _2. Above interface would be implemented by the sqlalchemy api. The file
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
    subscription_id = Column(String(36))
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
which would call nova extension to fetch data from database and we can get the 
output in command line.
1. Add nova client extension. The file should be placed into
<pyhon-novaclien>/novaclient/v1_1/contrib
```python

#[[file:$NOVA_CLIENT_ROOT$/novaclient/v1_1/contrib/server_models.py;action:copy]]
from novaclient import base
from novaclient import utils


class Server_Model(base.Resource):
    def delete(self):
        self.manager.delete(model=self)


class Server_ModelManager(base.ManagerWithFind):
    resource_class = base.Resource

    def list(self):
        return self._list('/thkcld-server_models', 'server_models')

    def get(self, server_model):
        return self._get('/thkcld-server_models/%s' % base.getid(server_model),
                         'server_model')

    def delete(self, server_model):
        self._delete('/thkcld-server_models/%s' % base.getid(server_model))

    def create(self, model_name):
        body = {'server_model':{'name':model_name}}
        return self._create('/thkcld-server_models', body, 'server_model')


@utils.arg('server_model_id', metavar='<server_model_id>', 
           help='ID of server model')
def do_server_model(cs, args):
    """
    Show a server model
    """
    server_model = cs.server_models.get(args.server_model_id)
    utils.print_dict(server_model._info)


def do_server_model_list(cs, args):
    """
    List networks
    """
    server_models = cs.server_models.list()
    utils.print_list(server_models, ['ID', 'Name','Created_at'])


@utils.arg('model_name', metavar='<model_name>',
           help='Server model name')
def do_server_model_create(cs, args):
    """
    Create a server model record
    """
    model = cs.server_models.create(args.model_name)
    utils.print_dict(model._info)


@utils.arg('server_model_id', metavar='<server_model_id>', 
           help='ID of server model')
def do_server_model_delete(cs, args):
    """
    Delete a server model
    """
    cs.server_models.delete(args.server_model_id)
    
```

**Tips**
  There is a name convension when mapping the command line to the python
action. e.g.
```shell
    nova server-model 1
```
The command "server-model" would be mapped to "do_server_model" subroutine 
in the extension file. 
The same thing, the command "server-model-list" wold be mapped to 
"do_server_model_list" suroutine in the extension file.

That's all. If all are right. Then you try the command:
```shell
   nova server-model 4
```
you should get the output like this:
```shell
    +------------+----------------------------+
    | Property   | Value                      |
    +------------+----------------------------+
    | created_at | 2013-12-07T07:11:24.000000 |
    | deleted    | 0                          |
    | deleted_at | None                       |
    | id         | 4                          |
    | name       | RD320                      |
    | updated_at | None                       |
    +------------+----------------------------+

    
```
