import os

from django.utils.translation import ugettext_lazy as _

DEBUG = True
TEMPLATE_DEBUG = DEBUG



# Specify a regular expression to validate user passwords.
# HORIZON_CONFIG = {
#     "password_validator": {
#         "regex": '.*',
#         "help_text": _("Your password does not meet the requirements.")
#     }
# }

LOCAL_PATH = os.path.dirname(os.path.abspath(__file__))

# Note: You should change this value
SECRET_KEY = 'dummy_secret_key'

# We recommend you use memcached for development; otherwise after every reload
# of the django development server, you will have to login again. To use
# memcached set CACHE_BACKED to something like 'memcached://127.0.0.1:11211/'
CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

# Send email to the console by default
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Or send them to /dev/null
#EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

# Configure these for your outgoing email host
# EMAIL_HOST = 'smtp.my-company.com'
# EMAIL_PORT = 25
# EMAIL_HOST_USER = 'djangomail'
# EMAIL_HOST_PASSWORD = 'top-secret!'

# For multiple regions uncomment this configuration, and add (endpoint, title).
# AVAILABLE_REGIONS = [
#     ('http://cluster1.example.com:5000/v2.0', 'cluster1'),
#     ('http://cluster2.example.com:5000/v2.0', 'cluster2'),
# ]

OPENSTACK_HOST = "127.0.0.1"
OPENSTACK_KEYSTONE_URL = "http://%s:5000/v2.0" % OPENSTACK_HOST
OPENSTACK_KEYSTONE_DEFAULT_ROLE = "Member"

# Disable SSL certificate checks (useful for self-signed certificates):
OPENSTACK_SSL_NO_VERIFY = True

# The OPENSTACK_KEYSTONE_BACKEND settings can be used to identify the
# capabilities of the auth backend for Keystone.
# If Keystone has been configured to use LDAP as the auth backend then set
# can_edit_user to False and name to 'ldap'.
#
# TODO(tres): Remove these once Keystone has an API to identify auth backend.
OPENSTACK_KEYSTONE_BACKEND = {
    'name': 'native',
    'can_edit_user': True
}

OPENSTACK_HYPERVISOR_FEATURES = {
    'can_set_mount_point': True
}

# OPENSTACK_ENDPOINT_TYPE specifies the endpoint type to use for the endpoints
# in the Keystone service catalog. Use this setting when Horizon is running
# external to the OpenStack environment. The default is 'internalURL'.
#OPENSTACK_ENDPOINT_TYPE = "publicURL"


# The number of Swift containers and objects to display on a single page before
# providing a paging element (a "more" link) to paginate results.
API_RESULT_LIMIT = 1000
API_RESULT_PAGE_SIZE = 20


# If you have external monitoring links, eg:
EXTERNAL_MONITORING = [ ]
LOGGING = {
        'version': 1,
        # When set to True this will disable all logging except
        # for loggers specified in this configuration dictionary. Note that
        # if nothing is specified here and disable_existing_loggers is True,
        # django.db.backends will still log unless it is disabled explicitly.
        'disable_existing_loggers': False,
        'formatters': {
            'debug': {
                'format': 'dashboard-%(name)s: %(levelname)s %(module)s %(funcName)s %(message)s'
            },
            'normal': {
                'format': 'dashboard-%(name)s: %(levelname)s %(message)s'
            },
        },
        'handlers': {
            'null': {
                'level': 'DEBUG',
                'class': 'django.utils.log.NullHandler',
                'formatter': 'debug'
                },
            'console': {
                # Set the level to "DEBUG" for verbose output logging.
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'debug'
                },
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': '/var/log/horizon/horizon.log',
                'formatter': 'normal'
                },
            'syslog': {
                'level': 'DEBUG',
                'facility': 'local1',
                'class': 'logging.handlers.SysLogHandler',
                'address': '/dev/log',
                'formatter': 'normal'
                },
            },
        'loggers': {
            # The logger name '' indicates the root of all loggers in Django, so
            # logs from any application in this project will go here.
            '': {
                'handlers': ['syslog'],
                'level': 'NOTSET',
                'propagate': True
                },
            # Logging from django.db.backends is VERY verbose, send to null
            # by default.
            'django.db.backends': {
                'handlers': ['null'],
                'level': 'DEBUG',
                'propagate': False
                },
            'horizon': {
                'handlers': ['syslog'],
                'level': 'DEBUG',
                'propagate': False
            },
            'openstack_dashboard': {
                'handlers': ['syslog'],
                'level': 'DEBUG',
                'propagate': False
            },
            'novaclient': {
                'handlers': ['syslog'],
                'level': 'DEBUG',
                'propagate': False
            },
           'glanceclient': {
                'handlers': ['syslog'],
                'level': 'DEBUG',
                'propagate': False
            },
            'keystoneclient': {
                'handlers': ['syslog'],
                'level': 'DEBUG',
                'propagate': False
            },
            'quantumclient': {
                'handlers': ['syslog'],
                'level': 'DEBUG',
                'propagate': False
            },
            'nose.plugins.manager': {
                'handlers': ['syslog'],
                'level': 'DEBUG',
                'propagate': False
            }
        }
}
LOGIN_URL='/dashboard/auth/login/'
LOGIN_REDIRECT_URL='/dashboard'

# The Ubuntu package includes pre-compressed JS and compiled CSS to allow
# offline compression by default.  To enable online compression, install
# the node-less package and enable the following option.
COMPRESS_OFFLINE = False
