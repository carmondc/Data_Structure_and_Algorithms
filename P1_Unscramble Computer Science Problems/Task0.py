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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
sending_text = texts[0][0]
receiving_text = texts[0][1]
timestamp_text = texts[0][2]
incoming_call = calls[-1][0]
receiving_call = calls[-1][1]
duration_call = calls[-1][2]
time_lasting = calls[-1][3]

print('First record of texts,', sending_text, "texts", receiving_text, "at time", timestamp_text)
print('First record of calls,', incoming_call, "calls ", receiving_call, "at time", duration_call, "lasting", time_lasting, "seconds")


# In[ ]:




