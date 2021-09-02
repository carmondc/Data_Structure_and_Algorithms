#!/usr/bin/env python
# coding: utf-8

# ## Problem 6: Union and Intersection
# 
# Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.
# 
# You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.
# 
# We have provided a code template below, you are not required to use it:

# In[1]:


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def get_head(self):
        return self.head
    
    def set_head(self, node):
        self.head = node
        
    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


# In[47]:


def union(element_1, element_2):
    union_set = set()
    i = 0
    j = 0
    
    while i < len(element_1) and j < len(element_2):
        if element_1[i] < element_2[j]:
            union_set.add(element_1[i])
            i += 1
        
        elif element_2[j] < element_1[i]:
            union_set.add(element_2[j])
            j += 1
            
        else:
            union_set.add(element_1[i])
            i += 1
            j += 1
            
    while i < len(element_1):
        union_set.add(element_1[i])
        i += 1
            
    while j < len(element_2):
        union_set.add(element_2[j])
        j += 1
            
    result = LinkedList()
    for element in union_set:
        result.append(element)

    return result
    
def intersection(element_1, element_2):
    i = 0
    j = 0
    inter_set = set()
    element_1.sort()
    element_2.sort()

    while i < len(element_1) and j < len(element_2):
        if element_1[i] < element_2[j]:
            i += 1
        
        elif element_2[j] < element_1[i]:
            j += 1
            
        else:
            inter_set.add(element_2[j])
            i += 1
            j += 1
            
    result = LinkedList()
    for element in inter_set:
        result.append(element)
            
    return result


# In[48]:


print("Testcase 1:")
element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]
print("union:", union(element_1, element_2))
print('intersection:', intersection(element_1, element_2),"\n")

print("Testcase 2:")
element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]
print("union:", union(element_1, element_2))
print('intersection:', intersection(element_1, element_2), "\n")

print("Testcase 3:")
element_1 = []
element_2 = []
print("union:", union(element_1, element_2))
print('intersection:', intersection(element_1, element_2), "\n")

print("Testcase 4:")
element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = []
print("union:", union(element_1, element_2))
print('intersection:', intersection(element_1, element_2))


# In[ ]:




