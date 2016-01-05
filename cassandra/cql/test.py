from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1', '127.0.0.2', '127.0.0.3'])
session = cluster.connect()
r = session.execute("create keyspace aj with replication = { 'class' : 'SimpleStrategy', 'replication_factor' : 3 };")
cluster.shutdown()
