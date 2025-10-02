# Linked Lists

Recall the following:

1. Recursive functions are able to reference themselves within the function.
2. What is actually happening is that we place a function call on a stack, 
until we reach the base case, and then return the results from the stack. 

Think of the recursive sum functions:

```
sum([1,2,3])

= (1 + sum([2,3]))     --> sum([2,3])

= (1 + (2 + sum([3]))) --> sum([3])
                           sum([2,3])
= (1 + (2 + (3)))
```

3. We investigated a variety of algorithms that directly involve a stack 
manipulation. 
4. We used the python list as a stack, but now we look into how one might 
implement a stack. 

This section discusses linked lists as the primitive data structure that 
can be utilized for a basick stack implementation. 

`Note that a linked list is not the same thing as an array.`

We may assume the following form for a List represented as nodes with pointers 
to other nodes.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

ls           = ListNode(0)
ls.next      = ListNode(1)
ls.next.next = ListNode(2)
print(ls.next.next.val)
```

## Search A Linked List

Given a list `L` (you may assume the head of the list) and a `key`, determine the node in the linked list that contains the `key`. For simplicity we always 
assume the key is somewhere in the list.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def search_list(L: ListNode, key: int) -> ListNode:
    while L and L.val != key:
        L = L.next
    return L

ls = ListNode(0)
ls.next = ListNode(1)
ls.next.next = ListNode(2)
found = search_list(ls, 2)
print(found.val)
</code></pre>
</details>

## Insert New Node After A Given Node

Given a `node` of a linked list, insert a `new_node` after this node.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def insert_after(node: ListNode, new_node: ListNode) -> None:
    new_node.next = node.next
    node.next = new_node

ls = ListNode(0)
ls.next = ListNode(1)
ls.next.next = ListNode(2)

insert_after(ls.next, ListNode(4))
print(
    ls.val,
    ls.next.val,
    ls.next.next.val,
    ls.next.next.next.val,
)
</code></pre>
</details>



   

