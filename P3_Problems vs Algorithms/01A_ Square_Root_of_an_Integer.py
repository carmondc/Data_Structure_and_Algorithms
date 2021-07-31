#!/usr/bin/env python
# coding: utf-8

# ## Finding the Square Root of an Integer
# 
# **Question**
# 
# Find the square root of the integer without using any Python library. You have to find the floor value of the square root.
# 
# For example if the given number is 16, then the answer would be 4.
# 
# If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.
# 
# The expected time complexity is O(log(n))

# In[119]:


import numbers

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    #If the number is not integer return none 
    if not isinstance(number, numbers.Number):
        return None
    
    # Base cases
    if (number == 0 or number == 1):
        return number
    if number < 0:
        return None
   
    
    left, right = 0, number//2
    while left <=right:
        pivot = left +(right - left)//2
        num = pivot * pivot
        if num > number:
            right = pivot -1
        elif num < number:
            left = pivot +1
        else: 
            return pivot
    return right


# In[125]:


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print("Pass" if (None == sqrt(None)) else "Fail")
print("Pass" if (None == sqrt(-1)) else "Fail")
print("Pass" if ( 3.0 == sqrt(10.5)) else "Fail")
print("Pass" if ( None == sqrt('a')) else "Fail")

