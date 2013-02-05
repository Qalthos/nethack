from __future__ import print_function, unicode_literals

class Nethack(object):
    def __init__(self, username, password, hostname, port):
        self.username = username
        self.password = password
        self.hostname = hostname
        self.port = port

        self.connection = NethackConnection(username, password, hostname, port)

    def __getattr__(self, func_name, *args, **kwargs):
        self.connection.send_message(func_name, *args, **kwargs)
