# Chapter 3

In the previous section you will have noticed that I provided
recursive and iterative versions to each example. To newcombers 
recursion may lok like magic, because the function is self-referential. 

We'll take a step back from recusion and look at the `data structure` that makes recursion possible in the first place. 
It's called the `stack`.

Think of it like a stack of plates. You can place them on top 
of each other, one-by-one. If you want to remove a plate, you 
are only allowed to move the top-most plate. 

When we place a plate on the stack we `append` it to the stack. 

When we remove a plate from the top of the stack we `pop` it off the stack.

We will show how to solve a variety of problems using stacks.

## Recursively Remove Elements From A Stack

You are given a stack of integers called `nums`. Write a function 
that recursively removes all the elements from `nums`.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def rec_remove_from_stack(nums: List[int]) -> None:
    if nums: # returns True if nums is not empty
        nums.pop() # remove plate from top of stack
        return rec_remove_from_stack(nums)

nums = [3,4,5,1]
print(nums)

rec_remove_from_stack(nums)
print(
    nums
)
</code></pre>
</details>

## Iteratively Remove Elements From A Stack

You are given a stack of integers called `nums`. Write a function 
that iteratively removes all the elements from `nums`.

<details>
<summary>Solution</summary>

<pre><code class="language-python">
def iter_remove_from_stack(nums: List[int]) -> None:
    while nums:
        nums.pop()

nums = [3,4,5,1]
print(nums)

iter_remove_from_stack(nums)
print(
    nums
)
</code></pre>
</details>





