from __future__ import print_function, unicode_literals

from nethack.connection import NethackFactory

class Nethack(object):
    def __init__(self, username, password, hostname, port):
        self.username = username
        self.password = password
        self.hostname = hostname
        self.port = port

        self.factory = NethackFactory(username, password)
        reactor.connectTCP(hostname, port)

    def __getattr__(self, func_name, *args, **kwargs):
        self.connection.send_message(func_name, *args, **kwargs)
