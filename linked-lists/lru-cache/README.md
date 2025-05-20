## LRU Cache

Implement the Least Recently Used (LRU) cache `class LRUCache`. The class should support the following operations:

- `LRUCache(int capacity)` - Initialize the LRU cache of size `capacity`.
- `int get(int key)` - Return the value corresponding to the `key` if the `key` exists, otherwise return `-1`.
- `void put(int key, int value)` - Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.

A key is considered used if a `get` or a `put` operation is called on it.

Ensure that `get` and `put` each run in O(1) average time complexity.
