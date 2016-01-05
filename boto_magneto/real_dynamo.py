# coding: utf-8
from boto.dynamodb2.fields import HashKey, RangeKey
from boto.dynamodb2.types import STRING, NUMBER
from boto.dynamodb2.layer1 import DynamoDBConnection
connection_data = {}
connection_data['aws_access_key_id'] = 'AKIAJ6PJI2SQGES3IDSL'
connection_data['aws_secret_access_key'] = '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'
connection_data['region'] = ''
connection_data['region'] = 'us-west-2'
conn = DynamoDBConnection(**connection_data)
conn = DynamoDBConnection(**connection_data)
connection_data['host'] = 'dynamodb.us-west-2.amazonaws.com'
conn = DynamoDBConnection(**connection_data)
conn
tables = conn.list_table()
tables = conn.list_tables()
from boto.dynamodb2.table import Table
users = Table.create('users', schema=[HashKey('name',
data_type=STRING), RangeKey('salary', data_type=NUMBER)],connection=conn)
users.put_item(data={'email':'aj', 'salary':1000})
users.put_item(data={'name':'aj', 'salary':1000})
users = Table.create('users', schema=[HashKey('name',
data_type=STRING), RangeKey('salary', data_type=NUMBER)],connection=conn)
conn.list_tables()
users.delete()
conn.list_tables()
conn.list_tables()
conn.list_tables()
conn.list_tables()
u = Table('users')
users.delete(connection=conn)
u = Table('users', connection=conn)
u
u.delete
conn.list_tables()
