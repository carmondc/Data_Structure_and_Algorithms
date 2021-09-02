#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    paths = []
    if suffix == '':
        print("Please provide suffix")
        return 
    
    if not os.path.exists(path):
        print("Invalid path")
        return 
    
    
    for p in os.listdir(path):
        if os.path.isfile(path + p):
            if p.endswith(suffix):
                paths.append(path + p)
        else:
            paths += find_files(suffix, path + p +'/')
                
    return paths


# In[2]:


## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
print (os.listdir("."))

# Let us check if this file is indeed a file!
print (os.path.isfile("./ex.py"))

# Does the file end with .py?
print ("./ex.py".endswith(".py"))


# In[4]:


path = 'testdir/'
print("\nTest1:")
print(find_files('.h', path))  
print("\nTest2:")
print(find_files('.c', path))  
print("\nTest3:")
print(find_files('.a', path))  
# Edge case
print("\nTest4:")
print(find_files('', path))  


# In[ ]:




