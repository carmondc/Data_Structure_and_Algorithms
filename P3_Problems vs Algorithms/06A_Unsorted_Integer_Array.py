#!/usr/bin/env python
# coding: utf-8

# ## Max and Min in a Unsorted Array
# 
# In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.
# 
# Bonus Challenge: Is it possible to find the max and min in a single traversal?

# In[58]:


class pair:
    def _init_(self):
        self.min = 0
        self.max = 0
    
    def get_min_max(ints):
        minmax = pair()
        n = len(ints)
        #If there is only one element then return it as min and max 
        if n== 1:
            minmax.max = arr[0]
            minmax.min = arr[0]
            return minmax
        #If there are more than one elements, then initialize min and max 
        if arr[0]>arr[1]:
            minmax.max = arr[0]
            minmax.min = arr[1]
        
        else:
            minmax.max = arr[1]
            minmax.min = arr[0]
            
        for i in range (2,n):
            if arr[i] > minmax.max:
                minmax.max = arr[i]
            elif arr[i] < minmax.min:
                minmax.min = arr[i]
        return minmax


# In[66]:


import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Pass" if ((-1, 1) == get_min_max([1, -1])) else "Fail")
print("Pass" if ((None, None) == get_min_max([])) else "Fail")
print("Pass" if ((0,4) == get_min_max([0,4])) else "Fail")
print("Pass" if ((100,100) == get_min_max([100])) else "Fail")

