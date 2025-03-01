# SYSTEM DESIGN & ARCHITECTURE ALGORITHMS

# 1. LOAD BALANCING ALGORITHM (Round Robin)
# Distributes incoming requests evenly across available servers.

class RoundRobinLoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get_server(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server
    
# Example Usage
servers = ["Server1", "Server2", "Server3"]
lb = RoundRobinLoadBalancer(servers)
for _ in range(6):
    print(f"Request handled by: {lb.get_server()}")    