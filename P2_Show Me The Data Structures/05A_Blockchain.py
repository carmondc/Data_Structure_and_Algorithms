#!/usr/bin/env python
# coding: utf-8

# ## Problem 5: Block Chain
# 
# A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a [SHA-256](https://en.wikipedia.org/wiki/SHA-2) hash, the [Greenwich Mean Time](https://en.wikipedia.org/wiki/Greenwich_Mean_Time) when the block was created, and text strings as the data.
# 
# Use your knowledge of linked lists and hashing to create a blockchain implementation.
# 

# In[12]:


from datetime import datetime, timezone
import hashlib


# In[30]:


class Block:
    def __init__(self, timestamp, data, previous_hash):
        """
        initial structure of the block class
        
        Args:
        self - refer to the class itself
        index - used to track the position of a block within the blockchain 
        timestamp - it inserts a timestamp for all the transactions performed
        data - it gives details of the transactions done
        previous_hash - it reference the hash of the previous block within the blockchain
        """
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None
        
    
    def calc_hash(self):
        """
        producing the crptographic hash of each block 
        """
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
    def get_previous_hash(self):
        return self.previous_hash
    
    def get_hash(self):
        return self.hash
    
    def __repr__(self):
        block = ('\n Block Attributes: \n timestamp: {}, \n data: {}, \n previous hash: {}, \n hash: {}'.format(str(self.timestamp), str(self.data), str(self.previous_hash), str(self.hash)))
        return block


# In[26]:


class Blockchain(object):
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, data):
        """
        Keep track the last addded block
        """
        # if the data is empty return No data
        if data is None or data == "":
            print("No data!")
            return 
        
        elif self.head is None:
            self.head = Block(datetime.now(timezone.utc), data, 0)
            self.tail = self.head
        
        else:
            self.tail.next = Block(datetime.now(timezone.utc), data, self.tail.hash)
            self.tail = self.tail.next
            
        return
    
    def to_list(self):
        """
        Print the blockchain
        """
        
        node = self.head
        output = []
        
        while node:
            output.append([node])
            node = node.next
            
        return output
    


# In[29]:


def main():
    print("Test 1:")
    
    block_1 = Blockchain()
    data1 = "First Blockchain in block"
    data2 = "Second Blockchain in block"
    data3 = "Third Blockchain in block"
    
    block_1.append(data1)
    block_1.append(data2)
    block_1.append(data3)
    
    print(block_1.to_list())
    
    print("\n Test 2:")
    print("Empty block")
    block_2 = Blockchain()
    block_2.append("")
    block_2.append("")
    print(block_2.to_list())
    
    print("\n Test 3:")
    print("Empty block")
    block_3 = Blockchain()
    block_3.append(None)
    block_3.append(None)
    print(block_2.to_list())
    
if __name__ == "__main__":
    main()


# In[ ]:




