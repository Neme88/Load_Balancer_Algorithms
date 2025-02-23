# 2. CONSISTENT HASHING
# Used for scalable load distribution in distributed systems.

import hashlib

class ConsistentHashing:
    def __init__(self, nodes=None, replicas=3):
        self.replicas = replicas
        self.ring = dict()
        self.sorted_keys = []

        if nodes:
            for node in nodes:
                self.add_node(node)

    def _hash(self, key):
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)

    def add_node(self, node):
        for i in range(self.replicas):
            hash_key = self._hash(f"{node}:{i}")
            self.ring[hash_key] = node
            self.sorted_keys.append(hash_key)
        self.sorted_keys.sort()

    def remove_node(self, node):
        for i in range(self.replicas):
            hash_key = self._hash(f"{node}:{i}")
            del self.ring[hash_key]
            self.sorted_keys.remove(hash_key)

    def get_node(self, key):
        hash_key = self._hash(key)
        for node_key in self.sorted_keys:
            if hash_key <= node_key:
                return self.ring[node_key]
        return self.ring[self.sorted_keys[0]]

# Example Usage
nodes = ["NodeA", "NodeB", "NodeC"]
ch = ConsistentHashing(nodes)
keys = ["User1", "User2", "User3", "User4"]
for key in keys:
    print(f"{key} is mapped to {ch.get_node(key)}")   
    