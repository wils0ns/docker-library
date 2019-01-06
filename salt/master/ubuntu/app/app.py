"""container entrypoint module"""
import os
import subprocess
import yaml
from time import sleep

SALT_LOG_LEVEL = os.environ.get('SALT_LOG_LEVEL', 'warning')
SALT_LOG_FILE_LEVEL = os.environ.get('SALT_LOG_FILE_LEVEL', 'warning')
SALT_MASTER_LOGFILE = '/var/log/salt/master'

# Salt API
SALT_API_PORT = os.environ.get('SALT_API_PORT', 8000)
SALT_API_USERNAME = os.environ.get('SALT_API_USERNAME', 'admin')
SALT_API_PASSWORD = os.environ.get('SALT_API_PASSWORD', 'admin')

SALT_MASTER_DEFAULT_CONFIG = {
    'log_level': SALT_LOG_LEVEL,
    'log_level_logfile': SALT_LOG_FILE_LEVEL,
    'rest_cherrypy': {
        'port': SALT_API_PORT,
        'ssl_crt': '/etc/pki/tls/certs/localhost.crt',
        'ssl_key': '/etc/pki/tls/certs/localhost.key',
        'log_access_file': '/var/log/salt/api.d/access.log',
        'log_error_file': '/var/log/salt/api.d/error.log',
        'expire_responses': False,
    },
    'external_auth': {
        'pam': {
            SALT_API_USERNAME: [
                '.*',
                '@wheel',
                '@runner',
                '@jobs',
            ]
        }
    }
}

def config_salt():
    """Configure salt-master and salt-api service"""

    process = subprocess.Popen(['salt-call', '--local', 'tls.create_self_signed_cert'])
    process.wait()

    with open('/etc/salt/master', 'w') as _file:
        yaml.dump(SALT_MASTER_DEFAULT_CONFIG, _file, default_flow_style=False)

    create_api_user()


def create_api_user():
    """Create salt-api default user"""
    process = subprocess.Popen([
        'salt-call', '--local', 'state.single',
        'user.present', 'name={}'.format(SALT_API_USERNAME),
        'password={}'.format(SALT_API_PASSWORD),
        'hash_password=True',
    ])
    process.wait()


def start_salt():
    """Start salt-syndic, salt-api and salt-master service"""
    subprocess.Popen(['salt-syndic', '--daemon'])
    subprocess.Popen(['salt-api', '--daemon'])
    salt_master = subprocess.Popen(['salt-master'])
    salt_master.wait()


def tail_events():
    """Tail salt events"""
    process = subprocess.Popen(['salt-run', 'state.event', 'pretty=True'], stdout=subprocess.PIPE)
    while True:
        print(process.stdout.readline())

if __name__ == '__main__':
    config_salt()
    start_salt()
