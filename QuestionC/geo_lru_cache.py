from collections import OrderedDict
import time
import random  # Import random for simulating network failures

class GeoLRUCache:
    def __init__(self, capacity: int):
        # Initialize cache with given capacity
        self.capacity = capacity
        self.cache = OrderedDict()
        self.access_times = {}
        self.regions = ['US', 'EU']  # Define regions
        self.replicated_data = {region: {} for region in self.regions}  # Replicated data for each region

    def get(self, key: str):
        # Get value from cache, update access frequency
        if key in self.cache:
            self.access_times[key] = time.time()
            value = self.cache[key]
            # Move the accessed item to the end (recently used)
            self.cache.move_to_end(key)
            # Simulate data replication to other regions (near real-time)
            self.simulate_data_replication(key, value)
            return value
        return None

    def put(self, key: str, value):
        # Add or update value in cache, handle eviction if needed
        if len(self.cache) >= self.capacity:
            # Evict least recently used item (first item in OrderedDict)
            self.cache.popitem(last=False)
        self.cache[key] = value
        self.access_times[key] = time.time()
        # Simulate data replication to other regions (near real-time)
        self.simulate_data_replication(key, value)

    def simulate_data_replication(self, key, value):
        # Simulate near real-time data replication to other regions with resilience
        for region in self.regions:
            if not self.is_network_resilient():
                self.replicated_data[region][key] = value
                time.sleep(0.1)  # Simulated delay for data replication

    def is_network_resilient(self):
        # Simulate network resilience with a probability of 10%
        return random.random() < 0.1  # Adjust probability as needed

    def expire_cache(self, expiration_time: float):
        # Expire cached items older than expiration_time (in seconds)
        current_time = time.time()
        keys_to_delete = [key for key, access_time in self.access_times.items()
                          if current_time - access_time > expiration_time]
        for key in keys_to_delete:
            del self.cache[key]
            del self.access_times[key]
            # Also remove replicated data
            for region in self.regions:
                self.replicated_data[region].pop(key, None)

    def get_size(self):
        # Get the current size of the cache
        return len(self.cache)

    def clear_cache(self):
        # Clear the cache and replicated data
        self.cache.clear()
        self.access_times.clear()
        for region in self.regions:
            self.replicated_data[region].clear()

    # Add other methods as needed
