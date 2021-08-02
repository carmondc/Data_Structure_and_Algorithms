#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[19]:


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
from collections import defaultdict

time_spent = dict()

for call in calls:
    if call[0] in time_spent:
        time_spent[call[0]] += int(call[3])
    else:
        time_spent[call[0]] = int(call[3])
        
    if call[1] in time_spent:
        time_spent[call[1]] += int(call[3])
    else:
        time_spent[call[1]] = int(call[3])

max_call_time = 0
max_call_number = None

for i in time_spent:
    if time_spent[i] >= max_call_time:
        max_call_time = time_spent[i]
        max_call_number = i
        
print(f"{max_call_number} spent the longest time, {max_call_time} seconds, on the phone during September 2016")
    


# In[ ]:




