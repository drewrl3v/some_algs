# Trees (DFS)

Firstly let's look into how we may represent a Tree.


```python
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right
```

Some of the most basic operations on trees are to insert new nodes:

```python
def insert_left(root: Node, new_node: Node) -> None:
    while root.left: # Traverse the left-half of the tree.
        root = root.left
    root.left = new_node
```