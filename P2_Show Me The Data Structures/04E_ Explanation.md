## Active Directory

To check whether a user is exists in a particular group or subgroup: 
* Create and Initialize Group class.
* Write `is_user_in_group` function:
    * Initialize the users group using `get_users()` function 
    * If the user is exissts in the users group then return True
    * Else check whether the user exists in any sub group:
        * Initialize the sub_group using `get_group()` function
        * Recursive through the sub_group if the user exists return True
    * Return False
    
**Complexity Analysis**

***Time complexity***
* Check if the user exists in the user list -> O(1)
* Iterating through the group_list -> O(g)
* Recursion for a tree of n nodes -> O(n)

Total => O(n* (1+g))

***Space complexity***
1. Input space:
    * users -> O(1)
    * group_list -> O(g)
    * input space for one iteration -> O(g+1)
    * input space fo depth iteration( k numbers of groups) -> O(depth * (g+1))
    
2. Auxiliary Space:
    * Recursive function is exhausted when it has reached the depth. Therefore O(depth) space is required in the call stack.
    
Total => O(depth * (g+1)) + O(depth) => O(depth * (g+1))
