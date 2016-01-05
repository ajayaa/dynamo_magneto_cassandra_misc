from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect()
session.set_keyspace('system')
rows = session.execute('select * from peers')
for row in rows:
    print row.peer, row.data_center
