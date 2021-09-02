#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys


# In[2]:


class Node(object):
    
    def __init__(self, data, freq):
        """
        Constructor for priority queue node
        
        Args:
        data -> data for priority queue
        freq -> frequency of data in priority queue
        """
        
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None
        
    def __lt__(self, other):
        return self.freq < other.freq
    
    def __gt__(self, other):
        return self.freq > other.freq
    
    def __eq__(self, other):
        return self.freq == other.freq
    
    def __str__(self):
        return '{}:{}'.format(self.data, self.freq)
    
    def display(self):
        for line in lines:
            print(line)       


# In[81]:


class MinHeap:
    def __init__(self):
        """
        Constructor for min heap.
        """
        self.data = []
        
    def up_heapify(self):
        child_index = len(self.data) - 1
        while child_index != -1:
            parent_index = self.get_parent(child_index)
            if parent_index == -1:
                return
            else:
                if self.data[parent_index] > self.data[child_index]:
                    self.data[parent_index], self.data[child_index] = (
                        self.data[child_index],
                        self.data[parent_index],
                    )
                    child_index = parent_index
                else:
                    child_index = -1
                    
    def down_heapify(self):
        child_index = 0
        while child_index != -1:
            left_index, right_index = self.get_child(child_index)
            if left_index == -1 and right_index == -1:
                return
            
            elif right_index == -1:
                if self.data[left_index] < self.data[child_index]:
                    self.data[left_index], self.data[child_index] = (
                        self.data[child_index],
                        self.data[left_index],
                    )
                    child_index = left_index
                else:
                    child_index = -1
            else:
                min_child = min(self.data[left_index], self.data[right_index])
                if min_child == self.data[left_index]:
                    min_child_index = left_index
                else:
                    min_child_index = right_index
                if min_child < self.data[child_index]:
                    self.data[min_child_index], self.data[child_index] = (
                        self.data[child_index],
                        self.data[min_child_index],
                    )
                    child_index = min_child_index
                else:
                    child_index = -1
                    
    def get_child(self, data_index):
        """
        Get child indices based on given data index.
        
        Args:
        data_idx: Index of the current element
        
        Returns:
        child element
        """
        left, right = 2 * data_index + 1, 2 * data_index + 2
        if left >= len(self.data):
            return -1, -1
        
        elif right >= len(self.data):
            return left, -1
        
        else:
            return left, right
        
    def get_parent(self, data_index):
        """
        Get parent indices based on given data index.
        
        Args:
        data_index: Index of the current element
        
        Returns:
        parent element
        """
        if data_index % 2 == 0:
            return (data_index - 1) // 2
        else:
            return data_index // 2
        
        
    def insert(self, element):
        """
        Insert element in the heap.
        Args:
            element: Element to be inserted in the heap
        Returns:
            None
        """
        self.data.append(element)
        if len(self.data) > 1:
            self.up_heapify()
            
    def pop(self):
        """
        Pop minimum element from the heap.
        Returns:
            Element on the top of the heap.
        """
        if len(self.data) == 0:
            return None
        
        elif len(self.data) == 1:
            element = self.data.pop(0)
            return element
        
        else:
            self.data[0], self.data[len(self.data) - 1] = (
                self.data[len(self.data) - 1],
                self.data[0],
            )
            element = self.data.pop(len(self.data) - 1)
            self.down_heapify
            return element
        
    def __len__(self):
        """
        Find number of elements in the heap.
        """
        return len(self.data)    


# In[101]:


def count_frequency(data):
    """
    Count character frequency based on the string.
    
    Args:
    data: Input string
    
    Returns:
    character frequency
    """
    character_freq = {}
    for char in data:
        if char in character_freq:
            character_freq[char] += 1
        else:
            character_freq[char] = 1
    return character_freq


# In[102]:


def build_huffman_tree(min_heap):
    """
    Function to create huffman tree.
    
    Args:
    min_heap: Minimum heap
   
    Returns:
    Root Node for huffman tree
    """
    if len(min_heap) == 1:
        left_node = min_heap.pop()
        new_node = Node(None, left_node.freq)
        new_node.left = left_node
        min_heap.insert(new_node)
    else:
        while len(min_heap) > 1:
            left_node = min_heap.pop()
            right_node = min_heap.pop()
            new_node = Node(None, left_node.freq + right_node.freq)
            new_node.left = left_node
            new_node.right = right_node
            min_heap.insert(new_node)
    return min_heap.data[0]


# In[103]:


def count_character_encoding(huffman_tree, prefix):
    """
    Encode data using huffman tree.
    
    Args:
    huffman_tree: huffman tree
    prefix: prefix string till this point
    
    Returns:
    characters encoding dictionary
    
    """
    characters_dict = {}
    if huffman_tree is None:
        return characters_dict
    
    characters_dict.update(count_character_encoding(huffman_tree.left, prefix + "0"))
    
    if huffman_tree.data is not None:
        characters_dict[huffman_tree.data] = prefix
    characters_dict.update(count_character_encoding(huffman_tree.right, prefix + "1"))
    
    return characters_dict


# In[104]:


def huffman_encoding(data):
    if len(data) == 0:
        print("No data for encoding!")
        return "", None
    
    character_freq = count_frequency(data)
    min_heap = MinHeap()
    for char, freq in character_freq.items():
        node = Node(char, freq)
        min_heap.insert(node)
        
    huffman_tree = build_huffman_tree(min_heap)
    character_encoding = count_character_encoding(huffman_tree, "")
    encoded_data = ""
    for char in data:
        encoded_data += character_encoding[char]
    return encoded_data, huffman_tree


# In[105]:


def is_root(node):
    """
    Helper function to check if a node is root.
    """
    return node.left is None and node.right is None

def _huffman_decoding(data, node):
    """
    Helper recursive function to traverse through the tree.
    """
    if is_root(node):
        return node.data, data
    
    #start traversing the huffman tree from root
    char = data[0]
    if char == "0":
        node_char, data = _huffman_decoding(data[1:], node.left)
    else:
        node_char, data = _huffman_decoding(data[1:], node.right)
    return node_char, data

def huffman_decoding(data, tree):
    #declare a blank decoded string
    decoded_string = ""
    while len(data) > 0:
        decoded_char, data = _huffman_decoding(data, tree)
        decoded_string += decoded_char
    print("huffman_decoding successful!")
    return decoded_string


# In[106]:


def test_case(data):
    codes = {}
    
    print("\n TESTCASE:")
    print("~"*sys.getsizeof(data))
    print("The size of the data is: {}".format(sys.getsizeof(data)))
    print("The content of the data is: '{}'".format(data), "\n")
    
    encoded_data, tree = huffman_encoding(data)
    print("encoding data")
    if encoded_data and len(encoded_data) > 0:
        print("The size of encoded data: {}".format(sys.getsizeof(int(encoded_data, base = 2))))
        print("Content of the encoded data:{}".format(encoded_data))
        
    else:
        print("Data was not encoded!")
    print("successful encode data \n")
    
    decoded_data = huffman_decoding(encoded_data, tree)
    print("decoding data")
    print(f"Size of the decoded data: {sys.getsizeof(decoded_data)}")
    print(f"Content of the encoded data: '{decoded_data}'")
    print("successful decode data \n")
    print("completed test case!")
    print()


# In[107]:


def main():
    
    # will just return Falses on an empty string
    sentence = ""
    test_case(sentence)

    sentence = "1"
    test_case(sentence)

    sentence = "AAA"
    test_case(sentence)
    
    sentence = "The bird is the word"
    test_case(sentence)

if __name__ == "__main__":
    main()


# In[ ]:




