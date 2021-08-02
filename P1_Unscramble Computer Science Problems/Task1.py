#!/usr/bin/env python
# coding: utf-8

# In[34]:


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

unique_num = set()

for text in texts:
    unique_num.add(text[0])
    unique_num.add(text[1])
    
for call in calls:
    unique_num.add(call[0])
    unique_num.add(call[1])
    
unique_num_count = len(unique_num)

print(f"There are {unique_num_count} different telephone numbers in the records.")

