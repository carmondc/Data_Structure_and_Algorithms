## LRU CACHE

The key to solve this problem is to use a double linked list. The double link list allows us to quickly move nodes because it has connections backwards and forwards through the list. The LRU Cache is a hash map of keys and double linked nodes. 

1. Create a class for Doubly LinkedList Node
2. Create a class for LRU Cahce
    * Initialize all variable
    * Implement the structure
        1. Get the key or check if the key is exists
            * If the cache hit, the get() operation return with the appropriate value
            * If the cache miss, the get() operation return -1
        2. Set the key
             * Set the value if the key is not present in the cache
             * If the cache is full, remove the least recently used entry first and then insert the key
        3. Delete the key
        4. Add the key
        
        

###  TIME COMPLEXITY
The size of the array will be the same as the capacity of the cache. 
1. get() -> O(1) 
2. set() -> O(1)

### SPACE COMPLEXITY
The space complexity is O(n) where n is the number of elements in the cache.


```python

```
