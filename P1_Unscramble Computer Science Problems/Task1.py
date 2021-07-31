#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

#create a set to store different telephone numbers in the records
telephone_numbers = set()

#Find all unique numbers in the texts dataset
for i in range(len(texts)):
    telephone_numbers.add(texts[i][0])
    telephone_numbers.add(texts[i][1])
    
# Find unique numbers in the calls dataset
for i in range(len(calls)):
    telephone_numbers.add(calls[i][0])
    telephone_numbers.add(calls[i][1])
    
#count the unique number 
count_unique_numbers = len(telephone_numbers)

print('There are {} different telephone numbers in the records'.format(count_unique_numbers))


# **Time Analysis Complexity**
# 
# For-loop over all in put O(n)
# 
# set.add(item) O(1)
# 
# The time complexity is O(n)
#     
# 

# In[ ]:




