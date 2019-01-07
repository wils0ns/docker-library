from pprint import pprint
from saltypie import Salt

for port in range(8000, 8002):
    print(port)
    salt = Salt('https://localhost:{}'.format(port), username='admin', passwd='admin', trust_host=True)
    pprint(salt.runner('manage.versions'))
