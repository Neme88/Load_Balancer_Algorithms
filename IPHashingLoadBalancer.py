import hashlib

class IPHashingLoadBalancer:
    def __init__(self, servers):
        self.servers = servers
