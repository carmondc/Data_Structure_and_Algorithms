#!/usr/bin/env python
# coding: utf-8

# ## Problem 1: Least Recently Used Cache
# We have briefly discussed caching as part of a practice problem while studying hash maps.
# 
# The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.
# 
# While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.
# 
# When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.
# 
# For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.
# 
# Your job is to use an appropriate data structure(s) to implement the cache.
# 
# In case of a cache hit, your get() operation should return the appropriate value.
# In case of a cache miss, your get() should return -1.
# While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
# All operations must take O(1) time.
# 
# For the current problem, you can consider the size of cache = 5.
# 
# Here is some boiler plate code and some example test cases to get you started on this problem:

# In[2]:


class DLLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


# In[31]:


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.dic = dict()
        self.head = DLLNode(0, 0)
        self.tail = DLLNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.dic:
            n = self.dic[key]
            self.delete_node(n)
            self.add_node(n)
            return n.value
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache
        # is at capacity remove the oldest item.    
        if key in self.dic:
            self.delete_node(self.dic[key])
        n = DLLNode(key, value)
        self.add_node(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self.delete_node(n)
            del self.dic[n.key]

    def delete_node(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def add_node(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail


# In[32]:


print('Testcase 1')
our_cache = LRU_Cache(5)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
our_cache.set(5, 5) 
our_cache.set(6, 6)
print(our_cache.get(3))   # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(())) #edge case


# In[33]:


print('Testcase 2')
our_cache_2 = LRU_Cache(2)
our_cache_2.set(1,1)
our_cache_2.set(2,2)
our_cache_2.set(3,3)
print(our_cache.get(1))
print(our_cache.get(2))
print(our_cache.get(3))
print(our_cache.get(0))
print(our_cache.get(-1))
print(our_cache.get(())) #edge case


# In[34]:


print('Testcase 3')
our_cache = LRU_Cache(25)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
print(our_cache.get(1))      
print(our_cache.get(2))       
print(our_cache.get(9))      
our_cache.set(25, 25) 
our_cache.set(6, 6)
print(our_cache.get(25))  
print(our_cache.get(())) #edge case


# In[35]:


print('Testcase 4')
our_cache = LRU_Cache(0)
our_cache.set(1, 1);
our_cache.set(2, 2);
print(our_cache.get(1))
print(our_cache.get(()))


# In[36]:


print('Testcase 5')
our_cache = LRU_Cache(-1)
our_cache.set(1, 1);
print(our_cache.get(1))
print(our_cache.get(()))


# In[ ]:




