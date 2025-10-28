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
    root.right = new_node
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
class Node:
    def __init__(self, val='', left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

def insert_left(root: Node, new_node: Node) -> None:
    while root.left: # Traverse the left-half of the tree.
        root = root.left
    root.left = new_node

def insert_right(root: Node, new_node: Node) -> None:
    while root.right: # Traverse the left-half of the tree.
        root = root.right
    root.right = new_node

def build_parse_tree(expr: str) -> Node:
    '''
    Input: a string for a mathematical expression
    Returns: the root node of the expression parsed
    '''

    # TODO: Make sure to handle spaces
    expr = list(expr)
    tree = Node(val='')
    p_stack = []
    p_stack.append(tree)
    cur_tree = tree

    for char in expr:
        if char == '(':
            insert_left(cur_tree, Node(''))
            p_stack.append(cur_tree)
            cur_tree = cur_tree.left
        elif char not in '+-*/)':
            cur_tree.val = char
            parent = p_stack.pop()
            cur_tree = parent
        elif char in '+-*/':
            cur_tree.val = char
            insert_right(cur_tree, Node(''))
            p_stack.append(cur_tree)
            cur_tree = cur_tree.right
        elif char == ')':
            p_stack.pop()

    return tree



'''
This should build the following tree:

(3+(4*5))

      +
   3    *
      4   5
'''

expression_tree = build_parse_tree("(3+(4*5))")
print(expression_tree.val)
print(expression_tree.left.val)
print(expression_tree.right.val)
print(expression_tree.right.left.val)
print(expression_tree.right.right.val)


</code></pre>
</details>


