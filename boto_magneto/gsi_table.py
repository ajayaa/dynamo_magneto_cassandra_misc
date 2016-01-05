users = Table.create('users', schema=[
    HashKey('uid'), # defaults to STRING data_type
    RangeKey('gid'),
], throughput={
    'read': 500,
    'write': 1500,
}, global_indexes=[
    GlobalAllIndex('group_index', parts=[
        HashKey('gid'),
        RangeKey('uid'),
    ],
    throughput={
        'read': 100,
        'write': 100,
    })
],
connection=conn
)

q_res = users.query_2(
gid__eq='g2',
index='group_index'
)

for res in q_res:
    print res['uid'], res['gid']
