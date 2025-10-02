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