## Dutch National Flag Problem

This problem is known as Dutch National Flag Problem which is sorting an array with three possible key values {0,1,2} that might correspond to the three colors of the Dutch National Flag. 
In this problem, we use thre pointer to track the rightmost boundary of zeros , the leftmost boundary of two , and the current element under the consideration . The idea of solution is to move the `front_index` pointer along the array, if `index_list[front_index] = 0` swap with `index_list[next_pos_0]`, vice versa. 
* Initialise the rightmost boundary of zeros: `next_pos_0 = 0`, leftmost boundary of twos: `next_pos_2 = len(array)-1` and the current element to consider: `front_index=0`
* While front_index <= next_pos_2:
    * if `index_list[front_index] = 0`: swap front_index and next_pos_0 elements and move both pointers to the right
    * if `index_list[front_index] = 1`: move pointer front_index to the right
    * if `index_list[front_index] = 2`: swap front_index and next_pos_2. Move pointer `next_pos_2` to the left.

###  Complexity Analysis

**Time complexity**

The time complexity is **O(n)** because only one traversal of the array is needed. 

**Space complexity**

The space complexity is constant **O(1)**


```python

```
