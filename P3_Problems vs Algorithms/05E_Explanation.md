## Autocomplete with Trie

A trie is a tree data strucutre used to store a string(a prefix). To implement a Trie class:
* Initialize the Trie class:
    * Initialize the Trie by adding a root node
    * `insert` function is to add a word to the trie
    * `find` function is to find the Trie node that represents the prefix
    
* Initialize the TrieNode class:
    * Initialize the child node in the Trie
    * `insert` function is to add a child node in to the trie
    * `suffixes` function 
        * Responsible to getting the suffix 
        * Return the suffix in a list
    * `_recursive` function 
        * support the recursive function 
        * The recursive procedure return a list of all complete words with a given prefix. The list is then traversed and the first character of the prefix are removed. 

## Complexity Analysis

**Time complexity**

The longest length of the word is N.
The height of the Trie -> N+1
Time complexityfor all insert, search is O(N) 

**Space complexity**

The space complexity is O(M*N*K)
