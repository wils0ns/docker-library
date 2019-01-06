# saltmaster

Useful environment variables:

| Variable | default value | Description |
| - | - | - |
| SALT_LOG_LEVEL | warning | Salt terminal log level |
| SALT_LOG_FILE_LEVEL | warning |Salt file log level |
| SALT_API_PORT | 8000 |Which port to run salt-api |
| SALT_API_USERNAME | admin | The user that will be created and granted salt-api admin rights |
| SALT_API_PASSWORD | admin | The password to be set to the salt-api admin user |


Default salt-master configuration:

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