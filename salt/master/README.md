# saltmaster

## Ubuntu

[![](https://images.microbadger.com/badges/version/cathaldallan/saltmaster:2017.7-ubuntu.svg)](https://github.com/codeminus/docker-library/blob/master/salt/master/2017.7/ubuntu/Dockerfile "2017.7-ubuntu")
[![](https://images.microbadger.com/badges/image/cathaldallan/saltmaster:2017.7-ubuntu.svg)](https://microbadger.com/images/cathaldallan/saltmaster:2017.7-ubuntu "2017.7-ubuntu")

[![](https://images.microbadger.com/badges/version/cathaldallan/saltmaster:2018.3-ubuntu.svg)](https://github.com/codeminus/docker-library/blob/master/salt/master/2018.3/ubuntu/Dockerfile "2018.3-ubuntu")
[![](https://images.microbadger.com/badges/image/cathaldallan/saltmaster:2018.3-ubuntu.svg)](https://microbadger.com/images/cathaldallan/saltmaster:2018.3-ubuntu "2018.3-ubuntu")

## CentOS
[![](https://images.microbadger.com/badges/version/cathaldallan/saltmaster:2017.7-centos.svg)](https://github.com/codeminus/docker-library/blob/master/salt/master/2017.7/centos/Dockerfile "2017.7-centos")
[![](https://images.microbadger.com/badges/image/cathaldallan/saltmaster:2017.7-centos.svg)](https://microbadger.com/images/cathaldallan/saltmaster:2017.7-centos "2017.7-centos")

[![](https://images.microbadger.com/badges/version/cathaldallan/saltmaster:2018.3-centos.svg)](https://github.com/codeminus/docker-library/blob/master/salt/master/2018.3/centos/Dockerfile "2018.3-centos")
[![](https://images.microbadger.com/badges/image/cathaldallan/saltmaster:2018.3-centos.svg)](https://microbadger.com/images/cathaldallan/saltmaster:2018.3-centos "2018.3-centos")

### Useful environment variables

| Variable | default value | Description |
|:- |:- |:- |
| SALT_LOG_LEVEL | warning | Salt terminal log level |
| SALT_LOG_FILE_LEVEL | warning |Salt file log level |
| SALT_API_PORT | 8000 |Which port to run salt-api |
| SALT_API_USERNAME | admin | The user that will be created and granted salt-api admin rights |
| SALT_API_PASSWORD | admin | The password to be set to the salt-api admin user |


### Default salt-master configuration

```python
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
```
