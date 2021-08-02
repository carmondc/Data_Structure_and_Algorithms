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


# In[82]:


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

areas_code = []

for call in calls:
    call_num = call[0]
    receive_num = call[1]
  
    
    if call_num.startswith('(080)'):
        if receive_num[0].startswith("(") :
            fixed_line = receive_num.find(")")
            areas_code.append(receive_num[0: fixed_line+1])
            
        elif (receive_num.startswith('7') or receive_num.startswith('8') or receive_num.startswith('9')):
            areas_code.append(receive_num[:4])
            
        elif receive_num.startswith('140'):
            areas_code.append("140")
        
sorted_areas_code = sorted(set(areas_code))        

print("The numbers called by people in Bangalore have codes:")
print(*sorted_areas_code, sep ='\n')


# In[89]:


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

count_call_others = 0
count_call_bangalore = 0

for i in range (len(calls)):
    if calls[i][0].startswith('(080)'):
        count_call_others += 1
        
        if calls[i][1].startswith("(080)") :
            count_call_bangalore += 1
    
# percentage of call           
percentage_calls = round((count_call_bangalore/count_call_others*100),2)         

print(f"{percentage_calls} percent of calls from fixed lines in Bangalore are calls to other fixed line in Bangalore to other fixed lines in Bangalore")


# In[ ]:




