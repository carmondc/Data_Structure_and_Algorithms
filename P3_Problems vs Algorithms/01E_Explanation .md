## Finding the Square Root of an Integer

Using binary search to find the square root of an integer. The value s could be define as $a^2 \leqslant$ number$<$$(a+1)^2$. For number $\geqslant$2, the square root is always smaller than x/2 and larger than 0:0<a<x/2. 
Since a is an integer, the problem goes down to the iteration over the sorted set of integer numbers.

* If x<2, return x
* Set the left boundary to 2, and the right boundary to x/2
* While left <= right:
     * Take pivot=left+(right-left)//2 as a guess. Compute pivot$*$pivot and compare it with number:
       * If pivot$*$pivot > x, move the right boundary (right = pivot -1)
       * Else, if pivot$*$pivot < x, move the left boundary (left = pivot +1)
       * Otherwise pivot$*$pivot` == number, return number
* Return right

###  Complexity Analysis

**Time complexity**

The binary search takes **O(log n)**.

**Space complexity**

The space complexity is constant **O(1)**
