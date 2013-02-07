from __future__ import print_function, unicode_literals

try:
    import ultrajson as json
except:
    import json

from twisted.internet import protocol
from twisted.protocols.basic import LineReceiver


class NethackConnection(LineReceiver):
    pass


class NethackFactory(protocol.Factory):
    pass
