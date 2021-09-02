#!/usr/bin/env python
# coding: utf-8

# ### Finding Files
# For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

# In[25]:


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


# In[26]:


## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
print (os.listdir("."))

# Let us check if this file is indeed a file!
print (os.path.isfile("./ex.py"))

# Does the file end with .py?
print ("./ex.py".endswith(".py"))


# In[40]:


path = 'testdir/'
print("\nTest1:")
print(find_files('.h', 'testdir/'))  
print("\nTest2:")
print(find_files('.c','testdir/'))  
print("\nTest3:")
print(find_files('.a', 'testdir/'))  
# Edge case
print("\nTest4:")
print(find_files('', 'testdir/'))
print("\nTest5:")
print(find_files('', 'testdir/subdir1/')) 
print("\nTest6:")
print(find_files('.c','testdir/t1.c/'))


# In[ ]:




