# Node class for B-tree
class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree (defines the range for the number of keys)
        self.leaf = leaf  # True if node is a leaf. Otherwise false
        self.keys = []  # List of keys
        self.children = []  # List of children nodes

    # A utility function to insert a new key in the subtree rooted with this node
    def insert_non_full(self, key):
        # Initialize index as index of rightmost element
        i = len(self.keys) - 1
        
        # If this is a leaf node
        if self.leaf:
            # Insert the new key at the correct position
            self.keys.append(None)  # Add space for the new key
            while i >= 0 and key < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key  # Insert the new key
        else:
            # Locate the child which will have the new key
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1
            
            # If the found child is full, split it
            if len(self.children[i].keys) == 2 * self.t - 1:
                self.split_child(i)
                
                # After split, the middle key goes up and the child splits into two
                if key > self.keys[i]:
                    i += 1
            
            self.children[i].insert_non_full(key)

    # A utility function to split the child y of this node
    def split_child(self, i):
        t = self.t
        y = self.children[i]
        z = BTreeNode(t, y.leaf)
        
        # New node will have t-1 keys
        z.keys = y.keys[t:(2 * t - 1)]
        y.keys = y.keys[0:(t - 1)]
        
        # Copy the last t children of y to z
        if not y.leaf:
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:t]
        
        # Insert a new child into this node
        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys.pop())

    # A function to traverse all nodes in a subtree rooted with this node
    def traverse(self):
        for i in range(len(self.keys)):
            if not self.leaf:
                self.children[i].traverse()
            print(self.keys[i], end=' ')
        
        if not self.leaf:
            self.children[len(self.keys)].traverse()

    # A function to search a key in the subtree rooted with this node
    def search(self, key):
        # Find the first key greater than or equal to key
        i = 0
        while i < len(self.keys) and key > self.keys[i]:
            i += 1
        
        # If the found key is equal to key, return this node
        if i < len(self.keys) and self.keys[i] == key:
            return self
        
        # If the key is not found and this is a leaf node, return None
        if self.leaf:
            return None
        
        # Search in the appropriate child
        return self.children[i].search(key)


# B-tree class
class BTree:
    def __init__(self, t):
        self.t = t  # Minimum degree
        self.root = BTreeNode(t, True)  # Initialize the root

    # Function to traverse all nodes in the B-tree
    def traverse(self):
        if self.root:
            self.root.traverse()

    # Function to search a key in this B-tree
    def search(self, key):
        if self.root is None:
            return None
        else:
            return self.root.search(key)

    # The main function that inserts a new key in this B-tree
    def insert(self, key):
        root = self.root
        
        # If the root node is full, the tree grows in height
        if len(root.keys) == 2 * self.t - 1:
            new_node = BTreeNode(self.t, False)
            new_node.children.append(self.root)
            new_node.split_child(0)
            new_node.insert_non_full(key)
            self.root = new_node
        else:
            root.insert_non_full(key)


# Example usage

# Create a B-tree with minimum degree 3
b_tree = BTree(3)

# Insert keys
for i in [10, 20, 5, 6, 12, 30, 7, 17]:
    b_tree.insert(i)

# Traverse the B-tree
print("B-tree traversal:")
b_tree.traverse()  # Output: 5 6 7 10 12 17 20 30

# Search for a key
key_to_search = 6
if b_tree.search(key_to_search):
    print(f"\nKey {key_to_search} found.")
else:
    print(f"\nKey {key_to_search} not found.")
