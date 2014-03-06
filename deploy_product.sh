sh i18n.sh
rm /usr/share/openstack-dashboard -rf
cp openstack-dashboard/ /usr/share/ -rf
chown apache:apache /usr/share/openstack-dashboard -R

rm /usr/lib/python2.6/site-packages/horizon -rf
cp horizon/ /usr/lib/python2.6/site-packages/ -rf

mv /etc/httpd/conf.d/ssl.conf /root/

cp openstack-dashboard/openstack_dashboard/templates/index.html /var/www/html/
cp openstack-dashboard/openstack_dashboard/templates/css /var/www/html/ -rf
cp openstack-dashboard/openstack_dashboard/templates/images /var/www/html/ -rf

service httpd restart
