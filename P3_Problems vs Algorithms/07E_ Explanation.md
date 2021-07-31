## HTTP Router using a Trie

For this problem, we are implementing HTTP Router using the Trie data structure. 
1. Implement the RouteTrie class:
    * Initialize the trie with an root node and a handler. This is the root path or home page node
    * `insert` function 
        * Assign the handler to the leaf(deepest) node of this path
        * Recursively add nodes
    * `find` function
        * Search a match for the path by navigate the trie starting from the root
        * Return the handler if match or None for no match

2. Implement The RouteTrieNode:
    * Initialize the node with the children and add a handler
    * `insert` function
        * Insert the node 

3. Implement the Router class that will wrap the Trie and handler
    * Create a new RouteTrie for holding the routes. Add a handler for page not found.
    * `add_handler` function:
        * Add a handler for a path
        * Split the path and pass the pass part
        * Insert a list to the Route Trie
    * `lookup` function
        * lookup path by parts and return the associated handler
        * If path is '/' return root path
        * If path is not found in node or path is not found in handler return not found
    * `split_path` function
        * split the path into parts for both the `add_handler` and `lookup` functions 
        * if the strings is empty, discard it
        * return path list
        
    

## Complexity Analysis

**Time complexity**

The worst-case runtime for creating a trie is a combination of `m`. 
The length of the longest key in the trie -> n
The worst case runtime of creating a trie is O(mn).
The time complexity of searching, inserting and deleting from a trie -> O(an)

**Space complexity**

The space complexity is O(n) where n is hte count or number of components in the path. 



```python

```
