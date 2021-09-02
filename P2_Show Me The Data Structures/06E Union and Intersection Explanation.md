## Union and Intersection

To solve this problem, I implemented a set and create a new linked list based on data holds in the set.

For union:
1. Initialize index variables i and j as 0
2. If element_1(i) is smaller than element_2(j), print element_1(i) and increment i
3. If element_1(i) is greater than element_2(j), print element_2(j) and increment j
4. If both are the same, print either one element and increment both i and j
5. Print remaining elements of the larger array
6. Convert the set to LinkedList

For intersection:
1. Initialize index variables i and j as 0
2. If element_1(i) is smaller than element_2(j), print element_1(i) and increment i
3. If element_1(i) is greater than element_2(j), print element_2(j) and increment j
4. If both are the same, print either one element and increment both i and j
5. Convert the set to LinkedList

### Time Complexity Analysis
**Union**

Converting set into LinkedList -> O(n)

**Intersection**

Converting set into LinkedList -> O(n)

### Space complexity 

The space complexity is O(n) becasue it return to LinkedList


```python

```
