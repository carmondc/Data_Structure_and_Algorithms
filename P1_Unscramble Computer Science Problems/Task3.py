#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[3]:


"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates. 
"""

def find_area_code(call_number):
    """
    This function is to get the area code of a call number
    
    Args:
    call_number(string) - a string representing a call numbers
    
    Return:
    area_code(string)
    """
    
    # Split the '(0' from the fixed line
    if call_number.startswith('(0'):
        return call_number.split(')')[0]+')'
        
    # Get the first four digits as the prefix of the mobile number
    if (' ' in call_number) and (call_number.startswith('7') or call_number.startswith('8') or call_number.startswith('9')):
        return call_number[:4]
    
    #Telemarketers area code '140'
    if call_number.startswith('140'):
        return '140'
    
    return None

#Create a set for Bangalore called code
bangalore_called_code = set()

#Find the area code
for i in range (len(calls)):
    if calls[i][0].startswith('(080)'):
        bangalore_called_code.add(find_area_code(calls[i][1]))
        
bangalore_code_list = list(bangalore_called_code)
bangalore_code_list.sort()
print('The numbers called by people in Bangalore have codes: {}'.format(bangalore_code_list))


# In[10]:


"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


bangalore_to_others = 0
bangalore_to_bangalore = 0
total_calls = 0

for i in range(len(calls)):
    #count all the calls made from a fixed line in Bangalore
    if calls[i][0].startswith('(080)'):
        bangalore_to_others += 1
        total_calls += 1
        #count all calls from a fixed line in Bangalore to a fixed line in Bangalore
        if calls[i][1].startswith('(080)'):
            bangalore_to_bangalore += 1
            total_calls += 1

# percentage of call s from fixed line in Bangalore to others            
percentage_calls = round((bangalore_to_bangalore/total_calls*100),2)            

print('{} percent of calls from fixed lines in Bangalore are calls to other fixed line in Bangalore to other fixed lines in Bangalore'.format(percentage_calls))


# **Time Complexity Analysis**
# 
# ***Part A***
# 
# Two for loop:
#     * For loop over all input -> O(n)
#     * SOrting a list -> O(n$*$log n)
#     
# Total = O(n$*$log n+n) = O(n$*$log n)
# 
# ***Part B***
# 
# For loop over all input O(n):
#     * String operation -> O(1)
#     * Incrementing a variable -> O(1)
#     
# Total = O(n*(1+1)) -> O(n)

# In[ ]:




