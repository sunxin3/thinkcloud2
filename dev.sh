rm /opt/stack/horizon/horizon -rf
rm /opt/stack/horizon/openstack_dashboard -rf
rm /opt/stack/horizon/static -rf
cp horizon/ /opt/stack/horizon/horizon -rf
cp openstack-dashboard/openstack_dashboard/ /opt/stack/horizon/openstack_dashboard -rf
cp openstack-dashboard/static/ /opt/stack/horizon/static -rf
sudo service apache2 restart
