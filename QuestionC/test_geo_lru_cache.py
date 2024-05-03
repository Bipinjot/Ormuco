import unittest
from geo_lru_cache import GeoLRUCache
import time

class TestGeoLRUCache(unittest.TestCase):
    def test_cache_initialization(self):
        # Test cache initialization with capacity
        cache = GeoLRUCache(5)
        self.assertEqual(cache.capacity, 5)

    def test_cache_get_put(self):
        # Test adding and retrieving data from cache
        cache = GeoLRUCache(3)
        cache.put("key1", "value1")
        cache.put("key2", "value2")
        self.assertEqual(cache.get("key1"), "value1")
        self.assertEqual(cache.get("key2"), "value2")

    def test_cache_update(self):
        # Test updating existing data in cache
        cache = GeoLRUCache(2)
        cache.put("key1", "value1")
        cache.put("key2", "value2")
        cache.put("key1", "new_value")
        self.assertEqual(cache.get("key1"), "new_value")

    def test_cache_replication(self):
        # Test data replication to other regions (simulated)
        cache = GeoLRUCache(3)
        cache.put("key1", "value1")
        time.sleep(0.2)  # Wait for replication simulation
        self.assertEqual(cache.replicated_data['US'].get("key1"), "value1")
        self.assertEqual(cache.replicated_data['EU'].get("key1"), "value1")

    def test_network_resilience(self):
        # Test network resilience simulation
        cache = GeoLRUCache(3)
        resilient_replications = 0
        for _ in range(100):
            cache.simulate_data_replication("key1", "value1")
            resilient_replications += "key1" not in cache.replicated_data['US'] or "key1" not in cache.replicated_data['EU']
        resilience_rate = resilient_replications / 1000
        self.assertLessEqual(resilience_rate, 0.2)  # Ensure resilience rate is within acceptable limits

    # Add more test cases as needed

if __name__ == "__main__":
    # Configure test runner with failfast and timeout
    runner = unittest.TextTestRunner(failfast=True, timeout=5)
    unittest.main(testRunner=runner)
