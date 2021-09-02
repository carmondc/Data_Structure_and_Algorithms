## Huffman Coding

To implement the logic for both encoding and decoding of data.

**PART A: Huffman Encoding**
1. Initialize class for Node for the Priority Queue 
2. Construct the class of MinHeap
3. Calculate the frequecy for each character based on the data
4. Create the huffman tree using MinHeap
    * Pop out two nodes with the minimun frequency from the priority queue
    * Create a new node with a frequency equal to the sum of the two nodes popped out. The new node will become an internal node in the Huffman tree. The lower frequency nodes become left child and the higher frequency nodes will become right child
5. Calculate the character encoding using huffman tree
    * Assign "0" to left child and "1" to right child
6. Calculate the huffman encoding and tree based on the data
    * generate the binary code for each character of the data.
    * traverse the path from root to the leaf node
    
**PART B: Huffman Decoding**
1. Create a function to check if the node is root
2. Create `_huffman_decoding` function to traverse throught the huffman tree
    * Traversing the HUffman tree from the root 
    * If the current bit of the encoded data is "0", move the left child
    * Else, move the right child
3. Huffman decoding
    * Declare a blank decoded string
    
### Time complexity analysis
1. Dictionary keep track of the character frequency -> O(n)
2. Priority Queue -> O(N)
3. Inserting in Priority Queue -> O(1)
4. Traverse between the huffman tree -> O(n)
5. Compressing data -> O(n)


```python

```
