class WeightedRoundRobinLoadBalancer:
    def __init__(self, server_weights):
        self.servers = []
        for server, weight in server_weights.items():
            self.servers.extend([server] * weight)  # Duplicate servers according to weight
        self.index = 0