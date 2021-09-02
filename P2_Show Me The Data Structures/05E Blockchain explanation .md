## Blockchain 

The key to solve this problem is to use linked list and hashing to create a blockchain. 

1. Create a class for the Block
    * Store information for the blockchain such as transaction time, data, and information about previous hash
    
2. Create a class for Blockchain
    * Initialize the head and tail for the blockchain
    * Implementing append to keep track of the added block
    * Implementing to_list to print the blockchain 

### Time Complexity Analysis
1. append blockchain -> O(1) 
2. to_list -> O(n)

### Space  Complexity Analysis

Space complexity takes an O(n) where n is depends on the amount of blocks that are added to the LinkedList.



```python

```
