import hashlib

class IPHashingLoadBalancer:
    def __init__(self, servers):
        self.servers = servers
    def get_server(self, client_ip):
        hash_value = int(hashlib.md5(client_ip.encode()).hexdigest(), 16)
        index = hash_value % len(self.servers)
        return self.servers[index] 

# Example Usage
servers = ["Server1", "Server2", "Server3"]
lb = IPHashingLoadBalancer(servers)
clients = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4"]
for client in clients:
    print(f"Client {client} is assigned to: {lb.get_server(client)}")