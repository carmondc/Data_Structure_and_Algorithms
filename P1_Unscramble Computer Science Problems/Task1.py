#!/usr/bin/env python
# coding: utf-8

# In[36]:


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

unique_num = []

for text in texts:
    unique_num.append(text[0])
    unique_num.append(text[1])
    
for call in calls:
    unique_num.append(call[0])
    unique_num.append(call[1])
    
sort_unique = sorted(set(unique_num))

print(f"There are {len(sort_unique)} different telephone numbers in the records.")


# In[ ]:




