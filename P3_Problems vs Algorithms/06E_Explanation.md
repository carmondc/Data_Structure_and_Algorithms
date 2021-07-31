##  Unsorted Integer Array

The problem is to implement search in **O(n)** time that gives an idea to use a linear seach. In the search, we will keep two pointer(`min` and `max`) to track the search scope. 
* Create a structure `pair` that contains `min` and `max` 
* Define get_min_max(ints) where ints is a list of integer containing more than one integers. 
    * If there is only one integer in the list then return the integer as min and max
    * If there is more than one integers in the list
        * Initialize the first and second integers as `min` and `max`.
        * Compare the next integer with the `min` and `max`. 
            * If the integer is smaller than the `min` then change the min. 
            * If the integer is larger than the `max` then change the max.
            * If the integer is not smaller than the `min` or larger than the `max`, ignore the integer
    * Return minmax

###  Complexity Analysis

**Time complexity**

The time complexity is **O(n)** because only one traversal of the array is needed. 

**Space complexity**

The space complexity is constant **O(1)**


```python

```
