#!/usr/bin/env python
# coding: utf-8

# ## Search in a Rotated Sorted Array
# 
# **Question**
# 
# You are given a sorted array which is rotated at some random pivot point.
# 
# Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
# 
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# 
# You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example:
# 
# Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

# In[41]:


import numbers
def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
     #If the input_list is not integer return none 
    if not isinstance(number, numbers.Number):
        return None
    
    # Base case if the input_list is empty return -1
    if len(input_list) == 0:
        return -1
    
    start, end = 0, len(input_list)-1
    while start <= end:
        mid = start + (end - start) //2
        if input_list[mid] == number:
            return mid
        elif input_list[mid] >= input_list[start]:
            if number >= input_list[start] and number < input_list[end]:
                end = mid -1
            else:
                start = mid+1
        else:
            if number <= input_list[end] and number > input_list[mid]:
                start = mid +1
            else:
                end = mid -1
    return -1


# In[2]:


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


# In[3]:


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# In[43]:


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], -1])
test_function([['a','n','b'], None])


# In[ ]:




