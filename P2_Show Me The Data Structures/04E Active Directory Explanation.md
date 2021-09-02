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
    


### Time complexity
* Check if the user exists in the user list -> O(1)
* Iterating through the group_list -> O(n)
* Recursion for a tree of n nodes -> O(n)

Total => O(n)

### Space complexity
Space complexity is O(n) 


```python

```
