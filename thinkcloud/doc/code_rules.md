# Background
  Since we are going to write some extensions for openstack to implement some
cutomized features.We need make our codes are clean and can be upgraded easily
with openstack version upgrade. By the old way, we checkout the openstack source
codes and cusomize them directly. It can satisfy current requirement but for the
long term, this way is very hard to sync up the upgrade of openstack from 
community. When openstack community release a new version. It's not easy to
migrate our customize codes to the lastest openstack version. To solve this 
issue, We put our customized codes into a different location and We add some
hooks into the openstack source codes. We use a script to weave our customized
code into those hooks. This way can make minimal changes to the openstack source
codes and the effort to sync openstack upgrade is also reduced.

# How "hooks" work
1. Add "hooks" into the openstack source codes which we want to do some changes.

  The hook is just a special python comments which would be recognized our 
deployment script. The hook is very similar to the 'MACRO' code in c/c++ source
codes. They would be replaced to the customized codes by the deployment script.
Here is an example of the hook in openstack source file:
```python
    #[[section1:start]]
    
    def physical_server_get(context,server_id):
        """Get a physical server or raise if it doesn't exist"""
        return IMPL.physical_server_get(context,server_id)
    
    #[[section1:end]]
    
    #[[section2:start]]
    #[[section2:end]]
```
    
There are two hooks in above codes. You can see the hooks actually are special
python comments. They are pairs with "start" and "end". Each pair represents a 
code block. It would be replace to real customized codes by deployment script.

2. definition the customized codes with the same hook tag in a new code 
repository.

Here is an exmple of customized codes:

```python

    #[[file:$NOVA_ROOT$/nova/db/api.py;action:weave]]

    #[[section1:start]]

    def physical_server_get(context,server_id):
        """Get a physical server or raise if it doesn't exist"""
        return IMPL.physical_server_get(context,server_id)
        
    def physical_server_create(context,server_id):
        """Get a physical server or raise if it doesn't exist"""
        return IMPL.physical_server_create(context,server_id)    

    #[[section1:end]]
```

3. How to map the customized file and original openstack source file.

  We need know the target file which should be subsituted. The target file 
location was defined in the customized file like this tag
    #[[file:$NOVA_ROOT$/nova/db/api.py;action:weave]]
The target file location is "$NOVA_ROOT$/nova/db/api.py.
The sring "$NOVA_ROOT$ would be replaced to the root directory of nova module
There is also "action" key word. Currently only two actions are supported.

* weave  (means the customized codes would be weave to the targe file)
* copy ( means the whole customized file would be copy to destination )

# Where is the deployment script
  the deployment script location is under  REPO/bin/deploy

# How to run the deplyment script
  You can run the deployment script by the following way
  
```
    ./deploy
```

  Normally, It's no harm to run it with several times.

    
    





    