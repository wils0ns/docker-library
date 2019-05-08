import os
import subprocess
import yaml


SALT_LOG_LEVEL = os.environ.get('SALT_LOG_LEVEL', 'warning')
SALT_LOG_FILE_LEVEL = os.environ.get('SALT_LOG_FILE_LEVEL', 'warning')

SALT_MINION_ID = os.environ.get('SALT_MINION_ID')
SALT_MASTER = os.environ.get('SALT_MASTER', 'salt')

salt_minion_config = {
    'log_level': SALT_LOG_LEVEL,
    'log_level_logfile': SALT_LOG_FILE_LEVEL,
    'master': SALT_MASTER
}

if SALT_MINION_ID:
    salt_minion_config.update({
        'id': SALT_MINION_ID
    })


def config_salt():
    with open('/etc/salt/minion', 'w') as _file:
        yaml.dump(salt_minion_config, _file, default_flow_style=False)


def start_salt():
    sp = subprocess.Popen(['salt-minion'])
    sp.wait()
 
   
if __name__ == '__main__':
    config_salt()
    start_salt()
