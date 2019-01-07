from pprint import pprint
from saltypie import Salt

salt = Salt('https://localhost:8000', username='admin', passwd='admin', trust_host=True)

pprint(salt.runner('manage.versions'))