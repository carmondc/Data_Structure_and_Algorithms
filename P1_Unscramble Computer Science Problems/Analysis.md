### Time Complexity Analysis

**Task 0 **

Accessing array via index has O(1) time compelxity.

**Task 1**

* For-loop over all input -> O(n)
* set.add(item) -> O(1)

Time complexity -> O(n)

**Task 2**

* For loop over all input O(n)
* First for loop:
    * Accessing array via index O(1)
    * Adding an element to dictionary O(1)  
* Second for loop:
    * Accessing an element to dictionary O(1)
 
Time complexity -> O(n)

**Task 3**

***Part A***

* Two for loop:
    * For loop over all input -> O(n)
    * Sorting a list -> O(n$*$log n)
    
Total = O(n$*$log n+n) = O(n$*$log n)

***Part B***

* For loop over all input O(n):
    * String operation -> O(1)
    * Incrementing a variable -> O(1)
    
Total = O(n*(1+1)) -> O(n)

**Task 4** 

Function Telemarketers(): O(n)

First and second for-loop:

    * Accessing array via index O(1)
    
    * Adding element to a set O(1)
    
Third for-loop: 

    * Checking for existence in a set O(1)
    
Sorting the list O(n$*$log n)

Printing a list O(n)

Total = O(n+n$*$log n+n) -> O(n$*$log n)



```python

```
