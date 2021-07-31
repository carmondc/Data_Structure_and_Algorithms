#!/usr/bin/env python
# coding: utf-8

# ## Rearrange Array Elements
# 
# **Question** 
# 
# Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).
# 
# for e.g. [1, 2, 3, 4, 5]
# 
# The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

# In[47]:


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    x = 0
    y = 0
    
    #Sorted input in reverse order
    sorted_input = mergesort(input_list)[::-1]
    
    for i in range(0, len(sorted_input),2):
        x = x * 10 + sorted_input[i]
        
    for j in range(1,len(sorted_input),2):
        y = y * 10 + sorted_input[j]
    
    return [x,y]


# In[48]:


def mergesort(items):
    #Base case 
    if len(items) <= 1:
        return items
    
    mid = len(items)//2
    left = items[:mid]
    right = items[mid:]
    
    #Call mergesort recursively with the left and right half
    left = mergesort(left)
    right = mergesort(right)
    
    #Merge our two halves and return
    return merge(left,right)

def merge(left, right):
    merged = []
    left_index = 0
    right_index =0
    
    #Move through the lists until we have exhausted one
    while left_index < len(left) and right_index < len(right):
        #If left's item is larger, append the right's item and increment the index
        #Otherwise, append the left's item and increment the index
        if left[left_index]  > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        
        else:
            merged.append(left[left_index])
            left_index += 1
            
    #Append any leftovers. Because we've broken from the while loop.
    # At least one is empty and the remaining:
    # a. sorted
    # b. all sort past our last element in merged
    
    merged += left[left_index:]
    merged += right[right_index:]
    
    return merged


# In[49]:


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# In[50]:


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[],[]])
test_function([[0],[0]])


# In[ ]:




