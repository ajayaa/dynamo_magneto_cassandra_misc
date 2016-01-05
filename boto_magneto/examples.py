# coding: utf-8
execfile('create_table.py')
conn.list_tables()
users.put_item(data={'name':'bj', 'salary':'1000'})
users = Table('users')
users = Table('users', connection=conn)
users.put_item(data={'name':'bj', 'salary':'1000'})
aj = users.get_item(name='aj')
aj
aj['name']
aj['salary']
dir(aj)
aj['lastname'] = 'agr'
aj.save()
aj['name'] = 'bj'
aj['salary']
aj.save()
aj['name']
aj.save(overwrite=True)
aj = users.get_item(name='aj')
aj['name']
aj['salary']
aj = users.get_item(name='bj')
aj['name']
aj['salary']
aj.delete()
from boto.dynamodb2.items import Item
cj = Item(users, data={'name':'cj', 'salary':1})
cj.save()
users = Table.create('users', schema=[HashKey('name',
data_type=STRING), RangeKey('salary', data_type=NUMBER)],connection=conn)
users = Table.create('users', schema=[HashKey('name',
data_type=STRING), RangeKey('salary', data_type=NUMBER)],connection=conn)
print """ajaya"""
x='dskjnsjd'
print """ajaya %s, """%table_name
print """ajaya %s, """%x
users = Table.create('users', schema=[HashKey('name',
data_type=STRING), RangeKey('salary', data_type=NUMBER)],connection=conn)
users = Table.create('users', schema=[HashKey('name',
data_type=STRING), RangeKey('salary', data_type=NUMBER)],connection=conn)
users = Table.create('users', schema=[HashKey('name',
data_type=STRING), RangeKey('salary', data_type=NUMBER)],connection=conn)
users = Table.create('users', schema=[HashKey('name',
data_type=STRING), RangeKey('salary', data_type=NUMBER)],connection=conn)
users = Table.create('users', schema=[HashKey('name',
data_type=STRING), RangeKey('salary', data_type=NUMBER)],connection=conn)
table_name="aj"
"""Attempt to change a resource which is still in
195             use: Duplicate table name: %s""" % table_name)
print """Attempt to change a resource which is still in
  use: Duplicate table name: %s""" % table_name
users = Table.create('users', schema=[HashKey('name',
data_type=STRING), RangeKey('salary', data_type=NUMBER)],connection=conn)
users = Table.create('users', schema=[HashKey('name',
data_type=STRING), RangeKey('salary', data_type=NUMBER)],connection=conn)
table-name
table_name
table_name['ad'] = as
table_name['ad'] = 'as'
users = Table.create('users', schema=[HashKey('name',
data_type=STRING), RangeKey('salary', data_type=NUMBER)],connection=conn)
users = Table.create('users', schema=[HashKey('name',
data_type=STRING), RangeKey('salary', data_type=NUMBER)],connection=conn)
users = Table.create('users', schema=[HashKey('name',
data_type=STRING), RangeKey('salary', data_type=NUMBER)],connection=conn)
users
aj
it = users.get_item(name='aj')
it
it['name']
it['salary']
it = users.get_item()
it = users.get_item()
it = users.get_item()
it = users.get_item()
users.put_item(data={'name':'kj', 'salary':'1000'})
users.put_item(data={'name':'kj', 'salary':1000})
users = Table.create('users', schema=[HashKey('name',
data_type=STRING), RangeKey('salary', data_type=NUMBER)],connection=conn)
users.delete()
users = Table.create('users', schema=[HashKey('name',
data_type=STRING), RangeKey('salary', data_type=NUMBER)],connection=conn)
users.delete()
users = Table.create('users', schema=[HashKey('name',
data_type=STRING), RangeKey('salary', data_type=NUMBER)],connection=conn)
users.delete()
users = Table.create('test', schema=[],connection=conn)
users = Table.create('users', schema=[HashKey('name',
data_type=STRING), RangeKey('salary', data_type=NUMBER)],connection=conn)
users = Table.create('users', schema=[HashKey('name',
data_type=STRING), RangeKey('salary', data_type=NUMBER)],connection=conn)
users = Table.create('users', schema=[HashKey('name',
data_type=STRING), RangeKey('salary', data_type=NUMBER)],connection=conn)
users = Table.create('users', schema=[HashKey('name',
data_type=STRING), RangeKey('salary', data_type=NUMBER)],connection=conn)
get_ipython().magic(u'date')
