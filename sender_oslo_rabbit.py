from oslo.config import cfg
from oslo import messaging

CONF = cfg.CONF
transport = messaging.get_transport(CONF,
         url='rabbit://guest:123@localhost:5672/')
notifier = messaging.Notifier(transport, "ajaya",driver='messaging', topic='mdb')
context = {}
payload = {"a":"b"}
import pdb; pdb.set_trace()
notifier.warn(context, "hi", payload)
