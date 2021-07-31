#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


# In[17]:


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

time_spent = {}
#Compute the total duration of the telephone numbers' calls
for i in range(len(calls)):
    call_duration = int(calls[i][3])
    
    #calculate for the calling telephone number
    if calls[i][0] not in time_spent:
        time_spent[calls[i][0]] = call_duration
    else:
        time_spent[calls[i][0]] += call_duration
    #calculate for the receiving telephone number
    
    if calls[i][1] not in time_spent:
        time_spent[calls[i][1]] = call_duration
    else: 
        time_spent[calls[i][1]] += call_duration
        
        
# Find the phone number with the longest calls duration
max_calls_duration = 0
phone_max_duration = None

# Find the first key which has the maximum value.
for key in time_spent:
    if time_spent[key] > max_calls_duration:
        max_calls_duration = time_spent[key]
        phone_max_duration = key

print('{} spent the longest time, {} seconds, on the phone during September 2016'.format(phone_max_duration, max_call_duration))


# **Time complexity Analysis**
# 
# For loop over all input O(n)
# First for loop:
#     * Accessing array via index O(1)
#     * Adding an element to dictionary O(1)
#     
# Second for loop:
#     * Accessing an element to dictionary O(1)
#     
# Time complexity -> O(n)

# In[ ]:




