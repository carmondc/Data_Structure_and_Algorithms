## Search in a Rotated Sorted Array

The problem is to implement a search in **O(log N)** time that gives an idea to use a binary search in a Rotated Sorted Array.In the binary search, we keep two pointer( `start` and `end`) to track the search scope. At each iteration, we reduce the search scope into half, by moving either the `start` or `end` pointer to the middle of the previous search scope. 
* Initiate the pointer `start` to `0`, and the pointer `end` to `len(input_list)-1`
* Perform standard binary. While `start <= end`:
    * Take an index in the middle `mid` as a pivot
    * If `input_list[mid] == number` return mid
    * There could be two situation:
        * Pivot element is larger than the first element in the array
            - If the target is located in the non-rotated subarray:
              go left: end = mid-1
            - Otherwise, go right: start = mid+1
        * Pivot element is smaller than the first element of the array
            - If the target is located in the non-rotated subarray:
              go right: start = mid+1
            - Otherwise go left: end = mid-1
    * If target not found, return -1



###  Complexity Analysis

**Time complexity**

The binary search takes **O(log n)**.

**Space complexity**

The space complexity is constant **O(1)**
