class WeightedRoundRobinLoadBalancer:
    def __init__(self, server_weights):
        self.servers = []
        for server, weight in server_weights.items():
            self.servers.extend([server] * weight)  # Duplicate servers according to weight
        self.index = 0
    
    def get_server(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server



# Example Usage
server_weights = {"Server1": 3, "Server2": 1, "Server3": 2}
lb = WeightedRoundRobinLoadBalancer(server_weights)
for _ in range(6):
    print(f"Request handled by: {lb.get_server()}")
    