cd horizon/locale/zh_CN/LC_MESSAGES/
msgfmt --statistics --verbose -o django.mo django.po 
service apache2 restart
