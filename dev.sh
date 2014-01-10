rm /opt/stack/horizon/horizon -rf
rm /opt/stack/horizon/openstack_dashboard -rf
rm /opt/stack/horizon/static -rf
cp /home/stack/thinkcloud2/horizon/ /opt/stack/horizon/horizon -rf
cp /home/stack/thinkcloud2/openstack-dashboard/openstack_dashboard/ /opt/stack/horizon/openstack_dashboard -rf
cp /home/stack/thinkcloud2/openstack-dashboard/static/ /opt/stack/horizon/static -rf
sudo service apache2 restart
