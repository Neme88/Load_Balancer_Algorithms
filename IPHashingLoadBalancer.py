import hashlib

class IPHashingLoadBalancer:
    def __init__(self, servers):
        self.servers = servers
    def get_server(self, client_ip):
        hash_value = int(hashlib.md5(client_ip.encode()).hexdigest(), 16)
        index = hash_value % len(self.servers)
        return self.servers[index] 