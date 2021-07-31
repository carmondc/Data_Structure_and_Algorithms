## Rearrange_Array_Elements

The maximum number can be formed from given digits(0-9) when the largest digit appears first, second largest digit appears second and so on. Finally the smallest digit appears in the end. We can extend the logic to solve this problem. First, sorting the specified array in descending order and construct two numbers (x,y) by picking alternative digits from the array i.e x is filled with digits at the odd indices and y is filled with digits at the even indices of the sorted array.

## Complexity Analysis

**Time complexity**

Sorting(for using mergesort) O(nlog(n)) 
2 for loops O(n/2 + n/2) => O(n) 
Total: O(nlog(n) + n = O(nlog(n))

**Space complexity**
Input space O(n) + Auxilliary space O(1) = O(n+1) = O(n)


