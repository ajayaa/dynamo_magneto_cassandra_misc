import boto
import boto.dynamodb
import logging
from boto.dynamodb2.fields import HashKey, RangeKey
from boto.dynamodb2.types import STRING, NUMBER
from boto.dynamodb2.layer1 import DynamoDBConnection
from boto.dynamodb2.fields import HashKey, RangeKey, GlobalAllIndex

logging.basicConfig(filename='boto_local.log', level=logging.DEBUG)
connection_data = {}
connection_data['aws_access_key_id'] = 'ca2d17196a8b47e588ecb50cbc0d30d5'
connection_data['aws_secret_access_key'] = 'f84dd875dde745b7a862a78a28f5b32e'
connection_data['is_secure'] = False
connection_data['host'] = 'localhost'
connection_data['port'] = 8000
connection_data['region'] = 'RegionOne'


conn = DynamoDBConnection(**connection_data)
tables = conn.list_tables()
print "your tables are: %s"%(tables)
