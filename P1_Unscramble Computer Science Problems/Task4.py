#!/usr/bin/env python
# coding: utf-8

# In[22]:


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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates
"""
telemarketers = set()
not_telemarketers = set()
    
#Telemarketers never send texts or receive texts
for text in texts:
    not_telemarketers.add(text[0])
    not_telemarketers.add(text[1])
        
#Telemarketers never receive incoming calls
for call in calls:
    not_telemarketers.add(call[1])
    
#Telemarketers make outgoing calls but never receive calls
for call in calls: 
    if call[0] not in not_telemarketers:
        telemarketers.add(call[0])
    
    
telemarketers_list = sorted(list(telemarketers))

print('These numbers could be telemarketers:')
print(*telemarketers_list, sep ='\n')


# In[ ]:




