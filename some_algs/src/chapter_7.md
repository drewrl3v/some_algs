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

```python
def insert_right(root: Node, new_node: Node) -> None:
    while root.right: # Traverse the left-half of the tree.
        root = root.right
    root.left = new_node
```

Some of the most basic applications of Binary Trees is to parse expressions.
For example consider the following mathematical expressions: 
(3 + (4*5))

The order of evaluation can be thought of as a tree where lower nodes have 
higher precedence. Let's read the expression from left to right and construct
the binary tree in steps:

```
--- Step 1
3

--- Step 2
    +
  /
3

--- Step 3
    +
  /   \
3      *

--- Step 4
    +
  /   \
3      *
      /  \
     4    5
```

## Problem 1

Given a mathematical expression such as: `(3 + (4*5))`, construct the parse 
tree. Note we will always give expressions with parenthesis to dictate the 
order of evaluation.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
# TODO
def build_parse_tree(expr: str) -> Node:
    '''
    Input: a string for a mathematical expression
    Returns: the root node of the expression parsed
    '''
    expr = list(expr)
    pass

</code></pre>
</details>


