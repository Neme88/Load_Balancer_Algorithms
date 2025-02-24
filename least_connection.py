class LeastConnectionsLoadBalancer:
    def __init__(self, servers):
        self.servers = {server: 0 for server in servers}  # Track active connections

    def get_server(self):
        server = min(self.servers, key=self.servers.get)  # Server with the fewest connections
        self.servers[server] += 1
        return server

    def release_connection(self, server):
        if self.servers[server] > 0:
            self.servers[server] -= 1