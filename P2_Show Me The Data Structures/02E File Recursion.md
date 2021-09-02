## File Recursion

For this problem, I use `os` library and the following functions:
1. os.listdir(directory) -> List all the files and folders
2. os.path.isfile -> Return True if the path is existing regular file
3. os.path.exists -> Return True if path refers to an existing path or an open file descriptor

Once the file is ready, I implement recursion in order to traverse throughout the directory. When the suffix is found, it appends it to path list in order to return the found files.

**Time Complexity Analysis**
1. Appending the list -> O(1)
2. Recursion -> O(k) time to run where k is the number of file


```python

```
