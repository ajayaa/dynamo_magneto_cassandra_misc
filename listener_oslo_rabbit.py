# TO use this install oslo.messaging in a venv.
from oslo.config import cfg
from oslo import messaging

CONF = cfg.CONF
transport = messaging.get_transport(CONF,
         url='rabbit://guest:123@localhost:5672/')
targets = [messaging.Target(topic='notifications')]

class NotificationEndpoint(object):
# The following function catches notification.info
    def info(self, ctxt, publisher_id, event_type, payload, metadata):
            print "ctct: %s" % ctxt
            print "publisher_id: %s" % publisher_id
            print "event_type: %s" % event_type
            print "payload: %s" % payload
            print "metadata: %s" % metadata

#    def error(self, ctxt, publisher_id, event_type, payload, metadata):
## The following function catches notification.error
#            print "context: %s" % ctxt
#            print "publisher_id: %s" % publisher_id
#            print "event_type: %s" % event_type
#            print "payload: %s" % payload
#            print "metadata: %s" % metadata


endpoints = [NotificationEndpoint()]
server = messaging.get_notification_listener(transport, targets, endpoints)
server.start()
#server.wait()
