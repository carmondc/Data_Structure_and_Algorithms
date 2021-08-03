#!/usr/bin/env python
# coding: utf-8

# In[3]:


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


# In[25]:


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
    list_call = call[0]
    list_receive = call[1]
    duration = call[3]
    
    if list_call in time_spent:
        time_spent[list_call] += int(duration)
    else:
        time_spent[list_call] = int(duration)
        
    if list_receive in time_spent:
        time_spent[list_receive] += int(duration)
    else:
        time_spent[list_receive] = int(duration)


max_call_number = max(time_spent, key = time_spent.get)

print(f"{max_call_number} spent the longest time, {time_spent.get(max_call_number)} seconds, on the phone during September 2016")
    


# In[ ]:




