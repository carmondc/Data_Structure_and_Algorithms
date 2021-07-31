#!/usr/bin/env python
# coding: utf-8

# In[11]:


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

def Telemarketers():
    #create a set of possible telemarketers
    possible_telemarketers = set()
    not_possible_telemarketers = set()
    
    #Telemarketers never send texts or receive texts
    for i in range (len(texts)):
        not_possible_telemarketers.add(texts[i][0])
        not_possible_telemarketers.add(texts[i][1])
        
    #Telemarketers never receive incoming calls
    for i in range(len(calls)):
        not_possible_telemarketers.add(calls[i][1])
    
    #Telemarketers make outgoing calls but never receive calls
    for i in range(len(calls)): 
        if calls[i][0] not in not_possible_telemarketers:
            possible_telemarketers.add(calls[i][0])
    
    return list(possible_telemarketers)

telemarketers_list = Telemarketers()
telemarketers_list.sort()

print('These numbers could be telemarketers: {}'.format(telemarketers_list))


# **Time Complexity Analysis**
# 
# Function Telemarketers(): O(n)
# 
# First and second for-loop:
# 
#     * Accessing array via index O(1)
#     
#     * Adding element to a set O(1)
#     
# Third for-loop: 
# 
#     * Checking for existence in a set O(1)
#     
# Sorting the list O(n$*$log n)
# 
# Printing a list O(n)
# 
# Total = O(n+n$*$log n+n) -> O(n$*$log n)
# 

# In[ ]:




